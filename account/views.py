from .serializers import UserSerializers, LoginSerializer, ChangePasswordSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from rest_framework import status
from .models import User
from meta.models import Account_Type
import jwt, datetime
from django.contrib.auth.hashers import check_password, make_password
secret_key = "temp_secret"


@api_view(["GET", "POST"])
def Register(request):
    if request.method == "GET":
        user = User.objects.all()
        serializer = UserSerializers(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        request.data["active_state"] = request.data["status"]
        request.data.pop("status")
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer.fields.pop("password")
            return Response(
                {
                    "data": serializer.data,
                    "message": "user created successfuly",
                    "success": True,
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"data": {}, "success": False, "error": {"message": serializer.errors}},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )


@api_view(["POST"])
def Login(request):
    if request.method == "POST":
        email = request.data["email"]
        password = request.data["password"]
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"data": {}, "message": serializer.errors, "success": False},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )

        user = User.objects.filter(email=email).first()
        if user is None:
            return Response(
                {"data": {}, "success": False, "error": {"message": "user not found"}},
                status=status.HTTP_404_NOT_FOUND,
            )

        if not user.check_password(password):
            return Response(
                {
                    "data": {},
                    "success": False,
                    "error": {"message": "password is incorrect"},
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        payload = {
            "id": user.id,
            "role": request.data['user_type'],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=7888),
            "iat": datetime.datetime.utcnow(),
        }
        access_token = jwt.encode(payload=payload, key=secret_key, algorithm="HS256")
        payload = {
            "id": user.id,
            "role": request.data['user_type'],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=30),
            "iat": datetime.datetime.utcnow(),
        }
        refresh_token = jwt.encode(payload=payload, key=secret_key, algorithm="HS256")
        return Response(
            {
                "data": {"access_token": access_token, "refresh_token": refresh_token},
                "message": "token created successfuly",
                "success": True,
            }
        )


@api_view(["GET"])
def UserView(request):
    if request.method == "GET":
        if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]
        else:
            raise AuthenticationFailed("authorization token missing")
        try:
            if auth_header.startswith("Bearer "):
                bearer_token = auth_header.split(" ", 1)[1]
                try:
                    payload = jwt.decode(bearer_token, secret_key, algorithms="HS256")
                    user = User.objects.get(id=payload["id"])
                    if not user:
                        raise ValueError("user not present")
                    serializer = UserSerializers(user)
                    serializer.fields.pop("password")
                    return Response(
                        {
                            "data": serializer.data,
                            "message": "user found",
                            "success": True,
                        },
                        status=status.HTTP_200_OK,
                    )
                except Exception as exp:
                    raise AuthenticationFailed(exp)
            else:
                return AuthenticationFailed("expecting bearer token")
        except Exception as exp:
            return Response(
                {"data": {}, "success": False, "error": {"message": exp.detail}},
                status=exp.status_code,
            )


@api_view(["POST"])
def ChangePassword(request):
    if request.method == "POST":
        password = request.data.get("password")
        confirm_password = request.data.get("confirm_password")
        new_password = request.data.get("new_password")

        if confirm_password != password:
            return Response(
                {
                    "data": {},
                    "success": False,
                    "error": {"message": "confirm password mismatch"},
                },
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )

        try:
            serializer = ChangePasswordSerializer(data=request.data)
            if serializer.is_valid():
                if "Authorization" in request.headers:
                    auth_header = request.headers["Authorization"]
                    if auth_header.startswith("Bearer "):
                        bearer_token = auth_header.split(" ", 1)[1]
                        try:
                            payload = jwt.decode(
                                bearer_token, secret_key, algorithms="HS256"
                            )
                            user = User.objects.filter(id=payload["id"]).first()
                            if not user:
                                return Response(
                                    {
                                        "data": {},
                                        "success": False,
                                        "error": {"message": "user not found in db"},
                                    },
                                    status=status.HTTP_404_NOT_FOUND,
                                )
                            if not check_password(password, user.password):
                                return Response(
                                    {
                                        "data": {},
                                        "success": False,
                                        "error": {"message": "entered wrong password"},
                                    },
                                    status=status.HTTP_400_BAD_REQUEST,
                                )
                            user.password = make_password(new_password)
                            user.save()
                            return Response(
                                {
                                    "data": {},
                                    "success": True,
                                    "message": "password password",
                                },
                                status=status.HTTP_202_ACCEPTED,
                            )
                        except Exception as exp:
                            raise AuthenticationFailed(exp)
                    else:
                        raise AuthenticationFailed("expected bearer token")
                else:
                    raise AuthenticationFailed("access token not present")
            else:
                return Response(
                    {
                        "data": {},
                        "success": False,
                        "error": {"message": serializer.errors},
                    },
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY,
                )
        except Exception as exp:
            return Response(
                {"data": {}, "success": False, "error": {"message": exp.detail}},
                status=exp.status_code,
            )


@api_view(["POST"])
def Logout(request):
    if request.method == "POST":
        try:
            if "Authorization" in request.headers:
                auth_header = request.headers["Authorization"]
                if auth_header.startswith("Bearer "):
                    bearer_token = auth_header.split(" ", 1)[1]
                    try:
                        payload = jwt.decode(
                            bearer_token, secret_key, algorithms="HS256"
                        )
                        user = User.objects.filter(id=payload["id"]).first()
                        if not user:
                            return Response(
                                "user not found in db", status=status.HTTP_404_NOT_FOUND
                            )

                        payload = {
                            "id": user.id,
                            "exp": datetime.datetime.utcnow()
                            + datetime.timedelta(seconds=1),
                            "iat": datetime.datetime.utcnow(),
                        }
                        access_token = jwt.encode(
                            payload=payload, key=secret_key, algorithm="HS256"
                        )
                        payload = {
                            "id": user.id,
                            "exp": datetime.datetime.utcnow()
                            + datetime.timedelta(seconds=1),
                            "iat": datetime.datetime.utcnow(),
                        }
                        refresh_token = jwt.encode(
                            payload=payload, key=secret_key, algorithm="HS256"
                        )
                        return Response(
                            {
                                "access_token": access_token,
                                "refresh_token": refresh_token,
                            },
                            status=status.HTTP_202_ACCEPTED,
                        )
                    except Exception as exp:
                        raise AuthenticationFailed(exp)
                else:
                    raise AuthenticationFailed("expected bearer token")
            else:
                raise AuthenticationFailed("access token not present")
        except Exception as exp:
            return Response(
                {"data": {}, "success": False, "error": {"message": exp.detail}},
                status=exp.status_code,
            )

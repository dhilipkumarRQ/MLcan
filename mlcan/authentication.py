from rest_framework.exceptions import AuthenticationFailed
import jwt

secret_key = "temp_secret"


def authenticate_api(func):
    def temp(request, *args, **kwargs):
        
        if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]
            if auth_header.startswith("Bearer "):
                bearer_token = auth_header.split(" ", 1)[1]
                try:
                    jwt.decode(bearer_token, secret_key, algorithms="HS256")
                    return func(request, *args, **kwargs)
                except Exception as exp:
                    raise AuthenticationFailed(exp)
            else:
                raise AuthenticationFailed("expecting bearer token")

        else:
            raise AuthenticationFailed("authorization token missing")   
        
    return temp

def auth_only_admin(func):
    def wrapper(request, *args, **kwargs):
        try:
            auth_header = request.headers["Authorization"]
            bearer_token = auth_header.split(" ", 1)[1]
            payload = jwt.decode(bearer_token, secret_key, algorithms="HS256")
            if payload['role'] == 'ADMIN':
                return func(request)
            else:
                raise AuthenticationFailed('only admin can access this api') 
        except Exception as exp:
            raise AuthenticationFailed(exp)

    return wrapper

def auth_only_emplopyee(func):
    def wrapper(request, *args, **kwargs):
        try:
            auth_header = request.headers["Authorization"]
            bearer_token = auth_header.split(" ", 1)[1]
            payload = jwt.decode(bearer_token, secret_key, algorithms="HS256")
            if payload['role'] == 'EMPLOPYEE':
                return func(request)
            else:
                raise AuthenticationFailed('only employee can access this api') 
        except Exception as exp:
            raise AuthenticationFailed(exp)

    return wrapper

def get_payload_from_token(request):
    if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]
            if auth_header.startswith("Bearer "):
                bearer_token = auth_header.split(" ", 1)[1]
                try:
                    return jwt.decode(bearer_token, secret_key, algorithms="HS256")
                except Exception as exp:
                    raise AuthenticationFailed(exp)
            else:
                raise AuthenticationFailed("expecting bearer token")
    else:
        raise AuthenticationFailed("authorization token missing")   
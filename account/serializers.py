from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import User
from meta.models import Account_Type


def is_valid_password(value):
    if len(value) < 8:
        raise ValidationError("password should contain min of 8 character")
    if value.isnumeric():
        raise ValidationError("password should atleast contains alphabet")
    if value.isalpha():
        raise ValidationError("password should atleast contains numbers")
    return value



class UserSerializers(serializers.ModelSerializer):

    user_type = serializers.SlugRelatedField(queryset=Account_Type.objects.all(), slug_field='type', required=True)

    class Meta:
        model = User
        fields = ["id","name", "email", "phone", "password", "active_state", "user_type"]


    def create(self, validated_data):
        password = validated_data.pop("password")
        user_instance = self.Meta.model(**validated_data)
        if password is not None:
            user_instance.set_password(password)
        user_instance.save()
        return user_instance

    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError("password should contain min of 8 character")
        if value.isnumeric():
            raise ValidationError("password should atleast contains alphabet")
        if value.isalpha():
            raise ValidationError("password should atleast contains numbers")
        return value

    def validate_phone(self, value):
        if len(value) < 10:
            raise ValidationError("phone number length should be 10")
        return value


class LoginSerializer(serializers.Serializer):
    user_type = serializers.SlugRelatedField(queryset=Account_Type.objects.all(), slug_field='type', required=True)
    class Meta:
        model = User
        fields = ['id','email','password','user_type']
        
    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError("password should contain min of 8 character")
        if value.isnumeric():
            raise ValidationError("password should atleast contains alphabet")
        if value.isalpha():
            raise ValidationError("password should atleast contains numbers")
        return value

class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=10, validators=[is_valid_password])
    confirm_password = serializers.CharField(
        max_length=10, validators=[is_valid_password]
    )
    new_password = serializers.CharField(max_length=10, validators=[is_valid_password])

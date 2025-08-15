from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id','username','email','password','first_name','last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }

        def create(self,validated_data):
            user = get_user_model().objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name']
            )

            user.set_password(validated_data['password'])
            user.save()
            return user

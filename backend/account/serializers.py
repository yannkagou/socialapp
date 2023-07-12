from rest_framework import serializers
from .models import User, FriendshipRequest

from rest_framework import serializers




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(
#         style={"input_type": "password"}, write_only=True)


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ("id","name", "email",)

        
class FriendshipRequestSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    
    class Meta:
        model = FriendshipRequest
        fields = ('id', 'created_by',)
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'name', 'nickname', 'birthday']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data): #유효성검사
        user = User.objects.create_user(**validated_data) 
        #create serializer 내장함수로 유저를 꾸림.
        #User.objects.create_user orm 사용
        #(**validated_data) 장고 serializer 내장함수 유효성검사 
        return user
from rest_framework import serializers
from api_v1.models import *
from datetime import datetime

class Friendserializers(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['vk_id','full_name','score']

class UserDetailSerializer(serializers.ModelSerializer):
    friends = Friendserializers(many=True)
    referals_count = serializers.IntegerField()
    class Meta:
        model = User
        exclude = ['reg_date', 'last_date', 'refer', 'date_of_birth']
        extra_kwargs = {'friends': {'required': False}}

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['vk_id','full_name','reg_date', 'last_date', 'refer', 'date_of_birth']

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['reg_date', 'last_date', 'score', 'buyed_updates', 'buyed_toys']


class ToyListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Toy
        fields = "__all__"
    
class UpdateListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Update
        fields = "__all__"




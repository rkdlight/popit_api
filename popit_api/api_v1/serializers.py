from rest_framework import serializers
from api_v1.models import *
from datetime import datetime


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['reg_date', 'last_date']


class ToyDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Toy
        fields = "__all__"
    

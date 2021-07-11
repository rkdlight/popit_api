from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from urllib.parse import urlparse, parse_qsl
from datetime import datetime, timezone, timedelta

from rest_framework.serializers import Serializer
from .service import is_request_valid
from rest_framework.views import  APIView
from rest_framework import generics
from django.db import models
from .models import *
from .serializers import *


class VKUserPermission(BasePermission):
    SECRET_KEY = "wvl68m4dR1UpLrVRli"
    life_time = 60*30
    def has_permission(self, request, view):

        if not 'HTTP-Referer' in request.headers and not 'vk_id' in request.data:
            return False
        
        if 'HTTP-Referer' in request.headers:
            url = request.headers['HTTP-Referer']
            query = dict(
                parse_qsl(
                    urlparse(url).query,
                    keep_blank_values=True
                )
            )
            if is_request_valid(query, self.SECRET_KEY):
                try:
                    session = Session.objects.get(pk=int(query['vk_user_id']))
                    session.created = datetime.now(timezone.utc)
                except:
                    Session.objects.create(vk_id=int(query['vk_user_id']))
                    
                return True
            else: 
                return False
        else:
            try:
                session = Session.objects.get(pk=int(request.data['vk_id']))
                if datetime.now(timezone.utc) -  session.created >= timedelta(seconds=self.life_time):
                    return False
                else:
                    return True
            except Exception as e:
                print(e)
                return False
            
            
class UserLoginView(APIView):

    permission_classes = [VKUserPermission]
    def post(self, request):
        user = User.objects.get(pk = int(request.data['vk_id']))
        last_active_time = user.last_date
        now = datetime.now(timezone.utc)
        seconds = (now - last_active_time).seconds
        user.score += user.coins_by_sec * seconds
        user.coins_available += user.coins_by_sec * seconds
        user.save()
        user = User.objects.all().annotate(referals_count = models.Count(models.F('referals'))).get(pk = int(request.data['vk_id']))
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)

class UserDetailView(generics.RetrieveAPIView):
    
    serializer_class = UserDetailSerializer
    permission_classes = [VKUserPermission]
    def get_queryset(self):
        queryset = User.objects.all().annotate(referals_count = models.Count(models.F('referals')))
        return queryset
 
class UserUpdateView(APIView):
    permission_classes = [VKUserPermission]
    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserUpdateSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [VKUserPermission]
    def perform_create(self, serializer):
        if 'refer' in self.request.data:
            serializer.save(active_toy=Toy.objects.get(pk=1), coins_available = 1)
        else:
            serializer.save(active_toy=Toy.objects.get(pk=1))



class ToyListView(generics.ListAPIView):
    queryset = Toy.objects.all()
    serializer_class = ToyListSerializer

class UpdateListView(generics.ListAPIView):
    queryset = Update.objects.all()
    serializer_class = UpdateListSerializer



# Create your views here.

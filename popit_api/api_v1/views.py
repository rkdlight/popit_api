from rest_framework.response import Response
from rest_framework.views import  APIView
from rest_framework import generics
from django.db import models
from .models import *
from .serializers import *


class UserDetailView(generics.RetrieveAPIView):
    
    serializer_class = UserDetailSerializer

    def get_queryset(self):
        queryset = User.objects.all().annotate(referals_count = models.Count(models.F('referals')))
        return queryset

class UserUpdateView(APIView):
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

    def perform_create(self, serializer):
        if self.request.data['refer']:
            serializer.save(active_toy=Toy.objects.get(pk=1), coins_available = 1)
        else:
            serializer.save(active_toy=Toy.objects.get(pk=1))



class ToyListView(generics.ListView):
    queryset = Toy.objects.all()
    serializer_class = ToyListSerializer

class UpdateListView(generics.ListView):
    queryset = Update.objects.all()
    serializer_class = UpdateListSerializer


# Create your views here.

from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('user/<int:pk>/', UserDetailView.as_view()),
    path('user/<int:pk>/update/', UserUpdateView.as_view()),
    path('user/', UserCreateView.as_view()),
    path('updates/', UpdateListView.as_view()),
    path('toys/', ToyListView.as_view()),
    path('login/', UserLoginView.as_view())
]
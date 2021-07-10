from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('users/<str:vk_id>/', UserDeatilView.as_view())
]
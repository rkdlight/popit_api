from rest_framework.response import Response
from rest_framework.views import  APIView

from .models import *
from .serializers import *


class UserDeatilView(APIView):

    def get(self, request, vk_id):
        user = User.objects.get(vk_id=vk_id)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)

    # def post(self, request):
        # if 
        # if User.objects.get(vk_id=vk_id)
        # serializer = UserDetailSerializer(request)


# Create your views here.

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,ListAPIView
from HspApp.serializers import CustomeUserSerializer
from rest_framework.permissions import IsAuthenticated

class UserCreateAPi(CreateAPIView):
	queryset = get_user_model().objects.all()
	serializer_class = CustomeUserSerializer
	


class UserListApi(ListAPIView):
	queryset = get_user_model().objects.all()
	serializer_class = CustomeUserSerializer
	







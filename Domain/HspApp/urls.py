from django.urls import path,include
from .Views.register_login_api import UserListApi,UserCreateAPi

urlpatterns = [
    path(r'register/', UserCreateAPi.as_view(), name='account-create'),
    path(r'user_list/', UserListApi.as_view(), name='list_users'),
]
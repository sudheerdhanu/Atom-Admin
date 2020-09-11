from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

User=get_user_model()
class CustomeUserSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(required=True,validators=[UniqueValidator(User.objects.all(),message='This mail is already exits')])
    mobile=serializers.IntegerField(required=True,validators=[UniqueValidator(User.objects.all(),message='This mobile number is already exits')])
    password=serializers.CharField(max_length=30)
    class Meta:
        model=User
        fields=('id','first_name','last_name','email','mobile','password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], validated_data['mobile'],
             validated_data['password'])
        return user



# from HspApp.serializers import CustomeUserSerializer
#
# data={
#     'first_name':'sudheer',
#     'last_name':'mandi',
#     'email':'ss@gmail.com',
#     'mobile':'123456',
#     'password':'123456'
# }
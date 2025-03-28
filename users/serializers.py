from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .models import StaffProfile, StudentProfile, Attendance

#Serializer classes here
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        #user = validated_data['user']
        user = get_user_model().objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        return user

class StaffProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffProfile
        fields = '__all__'

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'




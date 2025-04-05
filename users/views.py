from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from .models import *

# Create your views here.

#home view
def home(request):
    return render(request, 'home.html')

#register/login views
class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid:
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            
            return Response({'message':'User registration successfully', 'Token': token}, status.HTTP_201_CREATED)
        return ResourceWarning(serializer.errors, status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            token = Token.objects.get_or_create(user=user)
            return Response({'message':'User logged in successfully', 'token':token.key}, status.HTTP_200_OK)
        return Response({'error':'Invalid Credentials'}, status.HTTP_400_BAD_REQUEST)


class UserLogout(APIView):
    def post(self, request):
        try:
            request.user.auth_token.delete()
        except Exception:
            pass
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

#Custom Permission Teacher
class IsTeacher(IsAuthenticated):
    """Modified has_permission method to check if the user is staff
    this class only grants permission to the teachers and admin

    Args:
        IsAuthenticated (_type_): _description_
    """
    def has_permission(self, request, view):
        get_staff = StaffProfile.objects.filter
        return bool(request.user and get_staff(user=request.user))

#Teacher and Student APIview
class CreateStudentProfile(generics.CreateAPIView):
    authentication_classes = [IsAuthenticated]
    queryset = StudentProfile.objects.all()
    serializer_class = StaffProfileSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CreateStaffProfile(generics.CreateAPIView):
    authentication_classes = [IsAuthenticated,IsAuthenticated]
    queryset = StaffProfile.objects.all()
    serializer_class = StaffProfileSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class StudentModelView(ModelViewSet):
    authentication_classes = [IsAuthenticated,IsTeacher]
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

class TeacherModelView(ModelViewSet):
    authentication_classes = [IsAdminUser]
    queryset = StaffProfile.objects.all()
    serializer_class = StaffProfileSerializer


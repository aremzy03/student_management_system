from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from users.views import IsTeacher
from users.models import *
from users.models import *
from .models import Courses, Results, Enroll
from .serializers import CoursesSerializer, ResultsSerializer, EnrollmentSerializer
# Create your views here.

class CourseViews(ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    authentication_classes = [TokenAuthentication]
    #permission_classes = [IsTeacher]

class EnrollCourse(generics.CreateAPIView):
    queryset = Enroll.objects.all()
    serializer_class = EnrollmentSerializer
    authentication_classes = [TokenAuthentication]
    
    def create(self, request, *args, **kwargs):
        student = StudentProfile.objects.get(user=request.user)
        serialiser = self.get_serializer(data=request.data)
        serialiser.is_valid(raise_exception=True)
        
        enroll = serialiser.save(student=student)
        response_data = serialiser.data
        response_data['message'] = f"{student} successfully enrolled into the course"
        return Response(response_data, status=status.HTTP_201_CREATED)

class ViewEnrolledCourses(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    serializer_class = EnrollmentSerializer
    
    def get_queryset(self):
        user = self.request.user
        student = StudentProfile.objects.get(user=user)
        return Enroll.objects.get(student=student)

class Unenroll(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    serializer_class = EnrollmentSerializer
    
    def get_queryset(self):
        user = self.request.user
        student = StudentProfile.objects.get(user=user)
        return Enroll.objects.get(student=student)
	


    


    
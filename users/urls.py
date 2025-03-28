from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

#url routers here
router = DefaultRouter()
router.register(r'students', StudentModelView, basename='student-view')
router.register(r'teachers', TeacherModelView, basename='Teacher')

#Url patterns here
urlpatterns = [
    path('', home, name='home'),
    
    #registration and login
	path('register/', RegisterView.as_view(), name='user-register'),
    path('login/', UserLogin.as_view(), name='user-login'),
    
    #Teacher CRUD
    path('student/create', CreateStudentProfile.as_view(), name='create-student'),
    path('teacher/create', CreateStaffProfile.as_view(), name='create-staff'),
    path('', include(router.urls)),
    
]
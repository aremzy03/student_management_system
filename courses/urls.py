from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r"course", CourseViews, basename='courses')

urlpatterns = [
	path('', include(router.urls)),
    path('enroll/', EnrollCourse.as_view(), name='enroll'),
    path('enrolled/', ViewEnrolledCourses.as_view(), name='enrolled-courses'),
    path('unenroll/<int:pk>/', Unenroll.as_view(), name='unenroll'),
    
]

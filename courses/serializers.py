from rest_framework import serializers
from .models import Results, Courses, Enroll

#Serializers Here
class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = ['score, grade, remark']

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enroll
        fields = ['student', 'course']

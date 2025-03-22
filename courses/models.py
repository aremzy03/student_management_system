from django.db import models
from users.models import StudentProfile

# Create your models here.


class Results(models.Model):
    score = models.IntegerField()
    grade = models.CharField(max_length=1)
    remark = models.CharField(max_length=255)

    def __str__(self):
        return f"Score: {self.score}, Grade: {self.grade}, remark: {self.remark}."


class Courses(models.Model):
    name = models.CharField(max_length=150)
    student = models.ManyToManyField(StudentProfile)
    results = models.OneToOneField(Results, on_delete=models.CASCADE)
    coursecontent = models.TextField()

    def __str__(self):
        return self.name

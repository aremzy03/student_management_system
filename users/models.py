from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    profilepic = models.ImageField(upload_to=None)

    def __str__(self):
        return f"Student: {self.name}"


class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    profilepic = models.ImageField(upload_to=None)

    class Meta:
        roles = ["Teacher", "Admin"]

    def __str__(self):
        return f"Staff: {self.name}"


class Attendance(models.Model):
    student = models.OneToOneField(StudentProfile)
    date = models.DateField(auto_now_add=True)
    status = models.TextChoices("Present", "Absent")

    def __str__(self):
        return f"{self.student}'s attendance"

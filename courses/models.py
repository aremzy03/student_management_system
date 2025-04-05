from django.db import models

# Create your models here.

class Courses(models.Model):
    name = models.CharField(max_length=150)
    coursecontent = models.TextField()

    def __str__(self):
        return self.name


class Results(models.Model):
    course = models.ManyToManyField(Courses)
    score = models.IntegerField()
    grade = models.CharField(max_length=1)
    remark = models.CharField(max_length=255)
    student = models.OneToOneField('users.StudentProfile', on_delete=models.CASCADE)

    def __str__(self):
        return f"Score: {self.score}, Grade: {self.grade}, remark: {self.remark}."


class Enroll(models.Model):
    student = models.ForeignKey('users.StudentProfile', on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.student} is enrolled into {self.course}"    

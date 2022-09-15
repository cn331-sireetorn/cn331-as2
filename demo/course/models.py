from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    course = models.CharField(max_length=64)
    course_code = models.CharField(max_length=64)
    seat_quota = models.IntegerField()
    detail = models.CharField(max_length=500)
    semester = models.CharField(max_length=100)
    status = models.BooleanField()

    def __str__(self):
        return f"{self.course_code}"

class Enroll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return f"{self.user.username} {self.course} "
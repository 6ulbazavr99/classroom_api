from django.contrib.auth import get_user_model
from django.db import models

from course.models import Course

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=255)
    students = models.ManyToManyField(User, related_name='students', blank=True)
    mentor = models.ForeignKey(User, related_name='mentor', on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey(Course, related_name='course', on_delete=models.CASCADE, blank=True, null=True)
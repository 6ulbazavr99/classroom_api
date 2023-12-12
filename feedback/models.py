from django.contrib.auth import get_user_model
from django.db import models

from course.models import Course

User = get_user_model()


class Review(models.Model):
    owner = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='reviews', on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner} -> {self.course}'


class Like(models.Model):
    owner = models.ForeignKey(User, related_name='likes',
                              on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='likes', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['owner', 'course']
from django.db import models


class Subject(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    subjects = models.ManyToManyField(Subject, related_name='subjects', blank=True)
    requirements = models.ManyToManyField(Subject, related_name='requirements', blank=True)


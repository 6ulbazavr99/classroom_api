from django.contrib.auth import get_user_model
from rest_framework import serializers
from course.models import Course
from group.models import Group

User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

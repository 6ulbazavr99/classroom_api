from rest_framework import serializers

from course.models import Course, Subject


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


# from django_filters import rest_framework as filters

# class ProductFilter(filters.FilterSet):
#
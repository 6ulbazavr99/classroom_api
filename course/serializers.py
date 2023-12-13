from rest_framework import serializers

from course.models import Course, Subject


class CourseSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()

    def get_rating(self, obj):
        ratings = obj.ratings.all()
        total_ratings = ratings.count()
        if total_ratings > 0:
            rating_values = sum(rating.rating for rating in ratings) // total_ratings
        else:
            rating_values = 0
        return rating_values

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
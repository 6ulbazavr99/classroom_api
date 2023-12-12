import django_filters
from .models import Group


class GroupModelFilter(django_filters.FilterSet):
    field_name = django_filters.Filter(lookup_expr='exact')

    class Meta:
        model = Group
        fields = ['title', 'course']

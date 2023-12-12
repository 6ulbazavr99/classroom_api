from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend

from account.permissions import FirstLevelPermission, ThirdLevelPermission
from .filters import GroupModelFilter
from .models import Group
from .serializers import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GroupModelFilter

    def get_permissions(self):
        if self.action in permissions.SAFE_METHODS:
            return [FirstLevelPermission()]
        return [ThirdLevelPermission()]

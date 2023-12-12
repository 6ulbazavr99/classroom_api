from rest_framework import viewsets, permissions

from account.permissions import FirstLevelPermission, ThirdLevelPermission
from .models import Group
from .serializers import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get_permissions(self):
        if self.action in permissions.SAFE_METHODS:
            return [FirstLevelPermission()]
        return [ThirdLevelPermission()]

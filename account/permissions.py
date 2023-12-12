from rest_framework import permissions


class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            access_level = request.user.role.access_lvl
            return access_level >= self.required_access_level
        return False


class FirstLevelPermission(CustomPermission):
    required_access_level = 1


class SecondLevelPermission(CustomPermission):
    required_access_level = 2


class ThirdLevelPermission(CustomPermission):
    required_access_level = 3


class FourthLevelPermission(CustomPermission):
    required_access_level = 4


class FifthLevelPermission(CustomPermission):
    required_access_level = 5


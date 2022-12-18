from rest_framework import permissions


class IsInGroup(permissions.BasePermission):
    __full_access_groups = ["Avengers", "AmericanGods", "Xmen"]
    __read_only_groups = ["DoomPatrol", "TheTick", "FutureMan"]

    def has_permission(self, request, view):
        user_groups = list(request.user.groups.values_list('name', flat=True))
        for group in user_groups:
            if group in self.__full_access_groups:
                return True
        if request.method in permissions.SAFE_METHODS:
            for group in user_groups:
                if group in self.__read_only_groups:
                    return True
        return False

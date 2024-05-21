from rest_framework import permissions

class TweetReplyPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'partial_update', 'destroy']:
            return obj.owner.id == request.user.id
        return True

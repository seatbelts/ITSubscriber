from rest_framework import permissions

class EventoPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return True
        elif view.action in ['create', 'update', 'partial_update', 'destroy']:
            return request.user.is_authenticated() and request.user.is_staff
        else:
            return False

class ProyectoPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated()

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated()

class AlumnoPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_authenticated()
        elif view.action in ['retrieve', 'create']:
            return request.user.is_authenticated()
        elif view.action in ['update', 'partial_update', 'destroy']:
            return request.user.is_authenticated()
        else:
            return False

class EquipoPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated()

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated() and (obj.usuario == request.user or request.user.is_staff)

class MateriaPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return True
        elif view.action in ['create', 'update', 'partial_update', 'destroy']:
            return request.user.is_authenticated() and request.user.is_staff
        else:
            return False

class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            return True
        return request.user.is_authenticated()

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated() and (obj == request.user or request.user.is_staff)

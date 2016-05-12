from rest_framework import permissions

class AdminWritePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return request.user.is_authenticated()
        elif view.action in ['create', 'update', 'partial_update', 'destroy']:
            return request.user.is_authenticated() and request.user.is_staff
        else:
            return False

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
        return request.user.is_authenticated()

    def has_object_permission(self, request, view, obj):
        if view.action in ['list','retrieve', 'create']:
            return request.user.is_authenticated()
        elif view.action in ['update', 'partial_update', 'destroy']:
            return request.user.is_authenticated() and (obj.user == request.user or request.user.is_staff)
        else:
            return False

class EquipoPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated()

    #def has_object_permission(self, request, view, obj): Este es el que mencionaba, sobre cual es el uso de usuario ahora
        #return request.user.is_authenticated() and (obj.usuario == request.user or request.user.is_staff) usuario no se usa creo, se filtra por integrantes
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated()

class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            return True
        return request.user.is_authenticated()

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated() and (obj == request.user or request.user.is_staff)

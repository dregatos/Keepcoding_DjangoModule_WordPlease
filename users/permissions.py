# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si el usuario autenticado en request.user tiene
        permiso para realizar la acción (GET, POST, PUT o DELETE)
        """
        # no hace falta estar logeado para crear (POST) un usuario
        if view.action == "create":
            return True
        # el superusuario puede hacer todas las operaciones
        elif request.user.is_superuser:
            return True
        # si es un GET, PUT o DELETE tomo la decisión en has_object_permissions
        elif view.action in ['retrieve', 'update', 'destroy']:
            return True
        # por defecto no damos permiso
        else:
            # GET a /api/1.0/users/
            return False

    def has_object_permission(self, request, view, obj):
        """
        Define si el usuario autenticado en request.user tiene
        permiso para realizar la acción (GET, PUT o DELETE)
        sobre el object obj
        """
        # si es superadmin, o el usuario autenticado intenta
        # hacer GET, PUT o DELETE sobre su mismo perfil
        return request.user.is_superuser or request.user == obj


# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission
from datetime import date

class PostPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si el usuario autenticado en request.user tiene
        permiso para realizar la acción (GET, POST, PUT o DELETE)
        """
        # admin puede hacer lo que quiera
        if request.user.is_superuser:
            return True
        # cualquiera puede hacer un GET, el contenido recibido se decidirá en has_object_permission
        elif view.action in ['retrieve', 'list']:
            return True
        # sólo usuarios autenticados podrán, pero has_object_permissions decidirá sobre el permiso final
        elif view.action in ['create', 'update', 'destroy']:
            return request.user.is_authenticated()
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
        # si es superadmin -> True
        if request.user.is_superuser:
            return True
        # si intenta operar sobre uno de sus post -> True si soy dueño
        elif view.action in ['create', 'update', 'destroy']:
            return request.user == obj.blog.owner
        # podré leer un post si...
        elif view.action in ['retrieve', 'list']:
            # es público o si soy el dueño
            return obj.publication_date <= date.today() or request.user == obj.blog.owner
        # si no cumple nada de lo anterior
        else:
            False
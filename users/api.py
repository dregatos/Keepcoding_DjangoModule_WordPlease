# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from users.permissions import UserPermission
from users.serializers import UserSerializer


class UserViewSet (GenericViewSet):

    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    permission_classes = (UserPermission,)

    """
    # recuperar lista de usuarios == GET
    def list(self, request):
        # recupero todos los usuarios
        users = User.objects.all()
        self.paginate_queryset(users)  # pagino el resultado
        # Serializamos los objetos recibidos
        serializer = UserSerializer(users, many=True)  # 'many' indica que pasamos una lista, no un único objeto

        return self.get_paginated_response(serializer.data)  # devuelvo una respuesta paginada
    """

    # creamos un usuario == POST
    def create(self, request):
        serializer = UserSerializer(data=request.data) #TODOS LOS MÉTODOS REST VIENEN POR EL PARAMETRO 'DATA' DE LA REQUEST
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # recuperar detalle de un usuario == GET
    def retrieve(self, request, pk):
        # la función get_object_or_404 gestiona por nosotros el HttpResponseNotFound
        user = get_object_or_404(User, pk=pk)
        # para comprobar si has_object_permission, tengo que ejecutarlo a mano
        self.check_object_permissions(request, user)  # compruebo si el usuario autenticado puede hacer GET en este user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    # actualizamos info de usuario == PUT
    def update(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)  # compruebo si el usuario autenticado puede hacer PUT en este user
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # borramos usuario == DELETE
    def destroy(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)  # compruebo si el usuario autenticado puede hacer DELETE en este user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

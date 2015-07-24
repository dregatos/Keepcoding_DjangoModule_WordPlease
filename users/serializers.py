# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers

# Crearemos un serializar de usuarios

class UserSerializer(serializers.Serializer):

    # Las propiedades que (de)serializaremos
    # Es decir, los parámetros que tendremos que recibir para crear un nuevo usuario
    # y lo que devolveremos cuando nos pidan información de un usuario
    id = serializers.ReadOnlyField()        #sólo lectura
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        """
        Crear una instancia user a partir de los validated_data
        :param validated_data: Diccionario con datos de usuario
        :return: objeto user
        """
        # creamos una instancia vacía
        instance = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        """
        Actualiza una instancia de User a partir de los datos del diccionario validated_Data
        que contiene valores deserializados
        :param instance: objecto User a actualizar
        :param validated_data: diccionario
        :return: objeto User actualizado
        """
        # le asignamos los valores recibidos en el diccionario ya validado
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.email = validated_data.get('email')
        instance.username = validated_data.get('username')
        instance.set_password(validated_data.get('password'))  #set_password encripta la contraseña
        instance.save()

        return instance

    def validate_username(self, data):
        """
        Comprobamos si ya existe un usuario con ese username
        :param data: attribute username
        :return: data or exception
        """
        users = User.objects.filter(username=data)
        if not self.instance and len(users) != 0:
            raise serializers.ValidationError("Username already exists")
        elif self.instance and self.instance.username != data and len(users) != 0:
            raise serializers.ValidationError("New username already exists")
        else:
            return data
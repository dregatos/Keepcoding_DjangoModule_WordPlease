# -*- coding: utf-8 -*-
from django import forms
from blogs.models import Post


class PostForm(forms.ModelForm):
    """
    Formulario para el modelo Photo
    """
    class Meta:
        model = Post
        exclude = ['blog']
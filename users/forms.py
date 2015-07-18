# -*- coding: utf-8 -*-

from django import forms

class LoginForm(forms.Form):
    """
    FORMULARIO PARA LOGIN
    """
    usr = forms.CharField(label="Username")
    pwd = forms.CharField(label="Password", widget=forms.PasswordInput)

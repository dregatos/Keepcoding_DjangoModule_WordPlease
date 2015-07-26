# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import View
from blogs.models import Blog
from users.forms import LoginForm, RegistrationForm
from django.contrib.auth import logout as django_logout, authenticate, login as django_login

class LoginView(View):

    def get(self, request):
        error_messages = []
        form = LoginForm()
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)

    def post(self, request):
        error_messages = []
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                error_messages.append('Invalid username or password. Please, try again.')
            else:
                if user.is_active:
                    django_login(request, user)
                    return redirect(reverse('blog_detail', args=[username]))
                else:
                    error_messages.append('This user is not activated. Please, check your email.')

        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)

class LogoutView(View):

    def get(self, request):
        if request.user.is_authenticated():
            django_logout(request)
        return redirect('blogs_home')

class SignUpView(View):

    def get(self, request):
        error_messages = []
        form = RegistrationForm()
        context = {
            'errors': error_messages,
            'signup_form': form
        }
        return render(request, 'users/sign-up.html', context)

    def post(self, request):

        form = RegistrationForm(request.POST)
        if form.is_valid():

            new_user = form.save()

            blog_for_newUser = Blog()
            blog_for_newUser.owner = new_user
            blog_for_newUser.name = new_user.first_name + ' ' +new_user.last_name + '\'s Personal Blog'
            blog_for_newUser.save()

            return redirect(reverse('users_login'))
        else:
            context = {
                'signup_form': form
            }
            return render(request, 'users/sign-up.html', context)

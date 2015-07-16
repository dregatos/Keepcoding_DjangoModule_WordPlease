from django.shortcuts import render
from django.views.generic import View


class LoginView(View):

    def get(self, request):
        return render(request, 'users/login.html')

class LogoutView(View):

    def get(self, request):
        return render(request, 'blogs/home.html')

class SignUpView(View):

    def get(self, request):
        return render(request, 'users/sign-up.html')
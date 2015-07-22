# -*- coding: utf-8 -*-
from datetime import date
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.core.urlresolvers import reverse
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from blogs.forms import PostForm
from blogs.models import Post, Blog
from django.contrib.auth.decorators import login_required  #importamos el decorador de login_required

from django.db.models import Q

class HomeView(View):

    def get(self, request):
        """
        Fetch and Show latest 5 published posts.
        Post are shown in descending order taking into account their publication_date & creation date
        :param request:  HttpRequest
        :return: HttpResponse
        """
        posts = Post.objects.filter(publication_date__lte=date.today).order_by('-publication_date', '-created_at')
        if len(posts) > 0:
            context = {
                'posts_list': posts[:5]
            }
        else:
            context = {
                'message': ':( There isn\'t any published post'
            }

        return render(request, 'blogs/home.html', context)

class BlogListView(View):

    def get(self, request):
        """
        Fetch and Show all available blogs
        :param request: HttpRequest
        :return: HttpResponse
        """
        blogs = Blog.objects.order_by('-created_at')
        if len(blogs) > 0:
            context = {
                'blogs_list': blogs,
                'message': None
            }
        else:
            context = {
                'blogs_list': None,
                'message': 'No blog available'
            }

        return render(request, 'blogs/blogs_list.html', context)

class BlogDetailView(View):

    def get(self, request, username):
        """
        Fetch and Show blog's detail of the specified user
        :param request: HttpRequest
        :param username: The username of blog's owner
        :return: HttpResponse
        """
        blogs_list = Blog.objects.filter(owner__username__exact=username) #.prefeched_related('post').all()
        if len(blogs_list) == 1:
            posts = blogs_list[0].post_set.all().order_by('-publication_date', '-created_at')
            context = {
                'blog': blogs_list[0],
                'posts_list': posts
            }
            return render(request, 'blogs/blog_detail.html', context)
        else:
            return HttpResponseNotFound('The blog doesn\'t exist')

class PostDetailView(View):

    def get(self, request, username, pk):
        """
        Fetch and Show all available information of a post
        :param request: HttpRequest
        :param username: Blog's owner username
        :param pk: Post id
        :return: HttpResponse
        """
        #Handling errors using try-except
        try:
            post = Post.objects.get(blog__owner__username__exact=username, publication_date__lte=date.today, pk=pk) #.select_related('categories').all()
            #categories = post.category_set.all().order_by('name')
            context = {
                'post': post,
                #'categories': categories,
                'message': None
            }
        except ObjectDoesNotExist:
            context = {
                'post': None,
                'message': 'Post not found'
            }
        except MultipleObjectsReturned:
            context = {
                'post': None,
                'message': 'Houston, we have a problem'
            }

        return render(request, 'blogs/post_detail.html', context)

class NewPostView(View):

    @method_decorator(login_required())
    def get(self, request):
        form = PostForm()
        context = {
            'form': form,
            'success_message': ''
        }
        return render(request, 'blogs/new_post.html', context)

    @method_decorator(login_required())
    def post(self, request):

        success_message = ''

        blogs_list = Blog.objects.filter(owner__username__exact=request.user.username)
        if len(blogs_list) == 1:
            post_in_blog = Post()
            post_in_blog.blog = blogs_list[0] #asigno como propietario de la foto el usuario autenticado
            form = PostForm(request.POST, instance=post_in_blog) #basa la instancia de la petición en la que yo te paso. Mezcla campos!!
            if form.is_valid():
                new_post = form.save() #Crea, guarda y devuelve el objeto
                form = PostForm() #lo inicializamos tras guardar para que aparezca vacío de nuevo
                #Creamos nuestro mensaje de éxito con el link a la foto
                success_message = 'Guardado con éxito!!'
                success_message += '<a href="{0}">'.format(reverse('post_detail', args=[request.user.username, new_post.pk]))
                success_message += 'See post'
                success_message += '</a>'
            context = {
                'form': form,
                'success_message': success_message
            }
            return render(request, 'blogs/new_post.html', context)
        else:
            return HttpResponseNotFound('Houston, we have a problem')
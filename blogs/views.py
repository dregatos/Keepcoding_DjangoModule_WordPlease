from datetime import date
from django.shortcuts import render
from django.views.generic import View
from blogs.models import Post, Blog
from django.db.models import Q

class HomeView(View):

    def get(self, request):
        """
        Fetchs latest 5 published posts.
        Post are shown in descending order taking into account their publication_date & creation date
        :param request:  HttpRequest
        :return: HttpResponse
        """
        posts = Post.objects.filter(publication_date__lte=date.today).order_by('-publication_date', '-created_at')
        context = {
            'posts_list': posts[:5]
        }

        return render(request, 'blogs/home.html', context)

class NewPostView(View):

    def get(self, request):
        return render(request, 'blogs/new_post.html')

class BlogListView(View):

    def get(self, request):
        """
        Fetch all available blogs
        :param request: HttpRequest
        :return: HttpResponse
        """
        blogs = Blog.objects.order_by('-created_at')
        context = {
            'blogs_list': blogs
        }
        return render(request, 'blogs/blogs_list.html', context)

class BlogDetailView(View):

    def get(self, request, username):
        return render(request, 'blogs/blog_detail.html')

class PostDetailView(View):

    def get(self, request, username, pk):
        return render(request, 'blogs/post_detail.html')

from django.shortcuts import render
from django.views.generic import View

class HomeView(View):

    def get(self, request):
        return render(request, 'blogs/home.html')

class NewPostView(View):

    def get(self, request):
        return render(request, 'blogs/new_post.html')

class BlogListView(View):

    def get(self, request):
        return render(request, 'blogs/blogs_list.html')

class BlogDetailView(View):

    def get(self, request, username):
        return render(request, 'blogs/blog_detail.html')

class PostDetailView(View):

    def get(self, request, username, pk):
        return render(request, 'blogs/post_detail.html')

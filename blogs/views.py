from django.shortcuts import render
from django.views.generic import View
from blogs.models import Post


class HomeView(View):

    def get(self, request):
        """
        Fetchs all available posts and shows latest 5 published in descending order by creation date
        :param request:  HttpRequest
        :return: HttpResponse
        """
        posts = Post.objects.order_by('-created_at')
        context = {
            'posts_list': posts[:5]
        }

        return render(request, 'blogs/home.html', context)

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

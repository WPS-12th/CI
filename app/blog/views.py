from django.shortcuts import render

from .models import Post


def post_list(request):
    # config.urls
    # /posts/
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post-list.html', context)

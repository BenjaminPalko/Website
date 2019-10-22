from django.shortcuts import render, get_object_or_404

from .models import Post


def index(request):
    blog_post_list = Post.objects.order_by('-pub_date')
    context = {'blog_post_list': blog_post_list}
    return render(request, 'blog/index.html', context)


def post(request, post_title):
    post = get_object_or_404(Post, text_title=post_title)
    return render(request, 'blog/post.html', {'post': post})

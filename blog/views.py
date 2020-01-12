from django.shortcuts import render, get_object_or_404

from .models import Post


def index(request):
    blog_post_list = Post.objects.order_by('-pub_date')
    context = {'blog_post_list': blog_post_list}
    return render(request, 'blog/index.html', context)


def post(request, post_id, post_title):
    p = get_object_or_404(Post, text_title=post_title, id=post_id)
    return render(request, 'blog/post.html', {'post': p})

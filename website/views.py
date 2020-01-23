from django.shortcuts import render

from blog.models import Post


def index(request):
    blog_post_list = Post.objects.order_by('-pub_date')
    context = {'blog_post_list': blog_post_list}
    return render(request, 'index.html', context)

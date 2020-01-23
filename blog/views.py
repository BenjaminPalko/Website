from django.shortcuts import render, get_object_or_404

from .models import Post


def post(request, post_id, post_title):
    p = get_object_or_404(Post, text_title=post_title, id=post_id)
    return render(request, 'blog/post.html', {'post': p})

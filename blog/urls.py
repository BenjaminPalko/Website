from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:post_title>/', views.post, name='post'),
]

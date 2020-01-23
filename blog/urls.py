from django.urls import path

from . import views


urlpatterns = [
    path('<int:post_id>/<str:post_title>/', views.post, name='post'),
]

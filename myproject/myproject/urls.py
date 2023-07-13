from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('posts/', views.posts, name='posts'),
    path('admin/', admin.site.urls),
    path('posts/delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('create_post/', views.create_post, name='create_post'),
]

from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts


def posts(request):
    all_posts = Posts.objects.all()
    context = {
        'all_posts': all_posts,
        'success': 'All posts'
    }

    return render(request, 'posts.html', context)


def home(request):
    
    return render(request, 'blogTemplate.html')


def create_post(request):
    title = request.POST['title']
    content = request.POST['content']
    picture_url = request.POST['picture_url']
    post = Posts(title=title, content=content, picture_url=picture_url)
    post.save()

    all_posts = Posts.objects.all()
    context = {
        'all_posts': all_posts,
        'success': 'Post created succesfully'
    }

    return render(request, 'posts.html', context)

    
# Create your views here.

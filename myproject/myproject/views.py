from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Posts

all_records = Posts.objects.all()
print(all_records)
post_list = list(all_records)
print(post_list)
for post in post_list:
    print(post.title, post.content)
# records = []
# for record in all_records:
#         records.append[record]

def posts(request):
    context = {
        'message': {all_records},
    }
    return render(request, 'posts.html', context)


def home(request):
    
    return render(request, 'blogTemplate.html')


def create_post(request):
    # if request.method == 'POST':
    title = request.POST['title']
    content = request.POST['content']
    post = Posts(title=title, content=content)
    post.save()
    # return redirect('posts') 
    context = {
        'message': 'This is a dynamic message!',
    }

    return render(request, 'blogTemplate.html', context)

    
# Create your views here.

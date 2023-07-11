from django.shortcuts import render
from django.http import HttpResponse


def my_view(request):
    context = {
        'message': 'This is a dynamic message!',
    }
    return render(request, 'blogTemplate.html', context)

# Create your views here.

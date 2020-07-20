from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'nwakefi',
        'title' : 'Blog Post 1',
        'content': 'First post content',
        'date_posted' : '2018-08-27'
    },
    {
        'author' : 'nwakefi',
        'title' : 'Blog Post 2',
        'content': 'Second post content',
        'date_posted' : '2018-08-28'
    },
    {
        'author' : 'testuser',
        'title' : 'Blog Post 3',
        'content': 'New post content',
        'date_posted' : '2018-09-01'
    }
]


def home(request):
    context = {'posts':posts}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
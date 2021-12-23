from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
# Create your views here.


def home(request):
    # load all post from db(10)
    posts = Post.objects.all()[:11]
    data = {
        'posts': posts
    }
    return render(request, 'home.html', data)

def post(request, url):
    post = Post.objects.get(url=url)
    return render(request, 'posts.html', {'post': post})
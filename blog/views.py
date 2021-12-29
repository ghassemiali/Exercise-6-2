from django.shortcuts import render
from blog.models import Post
import datetime

def blog_view(request):
    x = datetime.timedelta(hours=3, minutes=30)
    now = datetime.datetime.now().astimezone(datetime.timezone(x))
    posts = Post.objects.filter(published_date__lte=now)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def single_view(request):
    return render(request, 'blog/blog-single.html')

def test_view(request, fname, lname, number):
    # http://127.0.0.1:8000/blog/ali/ghassemi/post-41/
    context = {'fname': fname, 'lname': lname, 'post_number': number}
    return render(request, 'blog/test.html', context)


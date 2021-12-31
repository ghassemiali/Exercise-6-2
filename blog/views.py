from django.shortcuts import render, get_object_or_404
from blog.models import Post
import datetime


# below function filter the posts which their published date is lower than or equal to NOW
def blog_view(request):
    x = datetime.timedelta(hours=3, minutes=30)
    now = datetime.datetime.now().astimezone(datetime.timezone(x))
    posts = Post.objects.filter(published_date__lte=now)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

# below function is for adding 1 to the counted_views in database for specific post
def add_one_in_views(post):
    post.counted_views += 1
    post.save()

# below function is for showing the only first post in the main blog page
# it also contains add_one_in_views for dynamic views counter
def single_view(request, pid):
    x = datetime.timedelta(hours=3, minutes=30)
    now = datetime.datetime.now().astimezone(datetime.timezone(x))
    posts = Post.objects.filter(status=1, published_date__lte=now)
    post_index = []
    for post in posts:
        post_index.append(post.id)
    post_index.sort()

    if post_index.index(pid) == 0:
        prev_post = 0
    else:
        prev_index = post_index.index(pid) - 1
        prev_post = get_object_or_404(posts, id=post_index[prev_index])


    if post_index.index(pid) == len(post_index) - 1:
        next_post = 0
    else:
        next_index = post_index.index(pid) + 1
        next_post = get_object_or_404(posts, id=post_index[next_index])


    post = get_object_or_404(posts, id=pid)
    context = {'post': post, 'prev_post': prev_post, 'next_post': next_post}
    
    add_one_in_views(post)
    return render(request, 'blog/blog-single.html', context)
    
def test_view(request, postnumber):
    post = get_object_or_404(Post, id=postnumber)
    context = {'post': post}
    return render(request, 'blog/test.html', context)


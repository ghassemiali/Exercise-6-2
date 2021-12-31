from os import name
from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='blog-home'),
    path('<int:pid>/', single_view, name='blog-single'),
    #path('post-<int:postnumber>/', test_view, name='test'),
]
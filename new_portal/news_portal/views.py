from django.views.generic import *
from .models import *


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')

class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import BlogPost


class BlogListView(ListView):

    queryset = BlogPost.objects.all()
    context_object_name = 'blog_posts'
    template_name = 'blog/blog_list.html'


class BlogDetailView(DetailView):

    model = BlogPost
    context_object_name = 'blog_detail'
    template_name = 'blog/blog_detail.html'

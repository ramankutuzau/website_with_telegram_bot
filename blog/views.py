from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


# Create your views here.

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("slug")).select_related('category')


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_recent'] = Post.objects.order_by('-id')[:3][::-1]  # добавляем словарь в контекст
        return context



def blog(request):
    context = {
        'post_list': Post.objects.all().order_by('-pk'),
        'post_recent': Post.objects.order_by('-id')[:3][::-1]
     }
    return render(request, 'blog.html',context)

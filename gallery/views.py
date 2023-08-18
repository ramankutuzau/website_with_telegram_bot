
from django.shortcuts import render

from .jobs.jobs import parse_instagram
from .models import InstagramPost

# Create your views here.


def gallery(request):
    # jobs.parse_instagram()
    posts = InstagramPost.objects.filter(is_active=True).order_by('-pk')
    return render(request, 'gallery.html', {'posts': posts})

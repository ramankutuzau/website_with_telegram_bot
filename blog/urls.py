from django.conf.urls.static import static
from django.urls import path, include

from .views import *
from config import settings

urlpatterns = [

    path('', blog, name='blog'),
    path('<slug:slug>/<slug:post_slug>/', PostDetailView.as_view(), name="post_single"),
    path('<slug:slug>/', PostListView.as_view(), name="post_list"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

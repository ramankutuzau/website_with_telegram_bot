from django.conf.urls.static import static
from django.urls import path, include

from .views import *
from config import settings

urlpatterns = [

    path('', index, name='index'),
    path('send-instagram/', send_instagram, name='send_instagram'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

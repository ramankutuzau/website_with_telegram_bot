from django.conf.urls.static import static
from django.urls import path, include

from .views import *

urlpatterns = [

    path('', gallery, name='gallery'),


    # path('', MiscalculationAPIList.as_view()),

    # path('home/', include('users.urls')),

]
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('', include('telegram_bot.urls')),
    path('gallery/', include('gallery.urls')),
    path('blog/', include('blog.urls')),

]

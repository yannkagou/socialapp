from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', include('post.urls')),
    path('api/', include('account.urls')),
    path('api/chat/', include('chat.urls')),
    path('api/search/', include('search.urls'))
]

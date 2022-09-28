from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace="blog")),
    path('comments/', include('django_comments_xtd.urls')),
]

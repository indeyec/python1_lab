
from django.contrib import admin
from django.urls import include, path
from register import views as v
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('main.urls')),
    path('',include('django.contrib.auth.urls')),
    path('polls/', include('polls.urls')),
    path('register/', v.register, name="register"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
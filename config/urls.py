from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('containers/', include('containers.urls')),
                  path('home/', include('units.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

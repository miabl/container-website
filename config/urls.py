from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from students import views
from units import views as unitview
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('containers/', include('containers.urls')),
                  path('units/', include('units.urls')),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('register/', views.register, name="register"),
                  path('', unitview.IndexView.as_view(), name='index'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
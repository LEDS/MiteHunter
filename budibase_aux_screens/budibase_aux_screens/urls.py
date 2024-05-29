from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('budibase_aux_screens.screens.urls')),
    path('accounts/login/',  auth_views.LoginView.as_view(), name='login'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

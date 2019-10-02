from django.contrib import admin
from django.urls import re_path, path, include
from django_registration.backends.one_step.views import RegistrationView
from users.forms import CustomUserForm
from core.views import IndexTemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/register/', 
         RegistrationView.as_view(
             form_class=CustomUserForm,
             success_url='/',
             ), name='django_registration_register'),

    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('api/', include('users.api.urls')),
    path('api/', include('adverts.api.urls')),
    
    path('api-auth/', include('rest_framework.urls')),
    path('api/rest-auth/', include('rest_auth.urls')),
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),

    re_path(r"^.*$", IndexTemplateView.as_view(), name='entry-point')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

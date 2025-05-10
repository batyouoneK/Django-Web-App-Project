"""
URL Configuration for cv_project
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

# Redirect view to send admin users directly to the custom CV admin page
def redirect_to_cv_admin(request):
    return redirect('cv_app:cv_admin')

urlpatterns = [
    # Redirect admin URL directly to our custom CV admin page
    path('admin/', redirect_to_cv_admin),
    
    # Keep admin login available for authentication
    path('admin/login/', admin.site.urls),
    
    # Include the CV app URLs (main website)
    path('', include('cv_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
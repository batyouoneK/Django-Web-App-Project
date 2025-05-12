"""
cv_project için URL Yapılandırması
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

# Admin kullanıcılarını doğrudan özel CV admin sayfasına yönlendirme görünümü
def redirect_to_cv_admin(request):
    return redirect('/cv-admin/')

urlpatterns = [
    # Admin URL'sini doğrudan bizim özel CV admin sayfamıza yönlendir
    path('admin/', redirect_to_cv_admin),
    
    # Kimlik doğrulama için admin girişini kullanılabilir tut
    path('admin/login/', admin.site.urls),
    
    # CV uygulaması URL'lerini dahil et (ana web sitesi)
    path('', include('cv_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from . import views
from . import admin_views

app_name = 'cv_app'

urlpatterns = [
    # Ana sayfa CV görünümü
    path('', views.home, name='home'),
    
    # İletişim sayfası
    path('contact/', views.contact, name='contact'),
    
    # Geliştirilmiş tek sayfa admin görünümü
    path('cv-admin/', admin_views.cv_admin_view, name='cv_admin'),
]
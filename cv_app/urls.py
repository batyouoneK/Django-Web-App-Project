from django.urls import path
from . import views
from . import admin_views

app_name = 'cv_app'

urlpatterns = [
    # The home page CV view
    path('', views.home, name='home'),
    
    # Improved single-page admin view
    path('cv-admin/', admin_views.cv_admin_view, name='cv_admin'),
]
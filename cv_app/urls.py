from django.urls import path
from . import views

app_name = 'cv_app'

urlpatterns = [
    # Home page (CV main page)
    path('', views.HomeView.as_view(), name='home'),
    
    # Project detail page
    path('project/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    
    # All projects page
    path('projects/', views.AllProjectsView.as_view(), name='all_projects'),
    
    # CV download functionality
    path('download-cv/', views.download_cv, name='download_cv'),
]
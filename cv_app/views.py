from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import PersonalInfo, Education, WorkExperience, Skill, Project, Certification


class HomeView(TemplateView):
    """
    Main view for the CV homepage displaying all resume sections.
    """
    template_name = 'cv_app/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get personal information (assuming there's only one entry)
        try:
            context['personal_info'] = PersonalInfo.objects.first()
        except PersonalInfo.DoesNotExist:
            context['personal_info'] = None
        
        # Get all other resume data
        context['education_list'] = Education.objects.all()
        context['experience_list'] = WorkExperience.objects.all()
        context['skill_list'] = Skill.objects.all()
        context['project_list'] = Project.objects.filter(is_featured=True)
        context['certification_list'] = Certification.objects.all()
        
        return context


class ProjectDetailView(DetailView):
    """
    Detailed view for a specific project.
    """
    model = Project
    template_name = 'cv_app/project_detail.html'
    context_object_name = 'project'


class AllProjectsView(TemplateView):
    """
    View to display all projects.
    """
    template_name = 'cv_app/all_projects.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context


def download_cv(request):
    """
    View to handle CV download functionality.
    Provides all CV data for print-friendly viewing and PDF creation.
    """
    context = {}
    
    # Get personal information (assuming there's only one entry)
    try:
        context['personal_info'] = PersonalInfo.objects.first()
    except PersonalInfo.DoesNotExist:
        context['personal_info'] = None
    
    # Get all other resume data
    context['education_list'] = Education.objects.all()
    context['experience_list'] = WorkExperience.objects.all()
    context['skill_list'] = Skill.objects.all()
    context['project_list'] = Project.objects.all()  # Include all projects, not just featured ones
    context['certification_list'] = Certification.objects.all()
    
    return render(request, 'cv_app/download_cv.html', context)
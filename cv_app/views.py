from django.shortcuts import render
from .models import PersonalInfo, Education, Experience, Skill

def home(request):
    """View function for the home page of the CV website"""
    # Get CV data from models
    personal_info = PersonalInfo.objects.first()  # Assume only one personal info entry
    education = Education.objects.all()
    experience = Experience.objects.all()
    skills = Skill.objects.all()
    
    # Context dictionary to pass to the template
    context = {
        'personal_info': personal_info,
        'education': education,
        'experience': experience,
        'skills': skills,
    }
    
    # Render the CV template with the data
    return render(request, 'cv_app/home.html', context)
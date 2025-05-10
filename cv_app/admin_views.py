from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.core.paginator import Paginator

from .models import PersonalInfo, Education, Experience, Skill
from django import forms

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        widgets = {
            'institution': forms.TextInput(attrs={'class': 'form-control'}),
            'degree': forms.TextInput(attrs={'class': 'form-control'}),
            'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
        widgets = {
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
        }

@staff_member_required
def cv_admin_view(request):
    """
    Unified CV admin view with all forms and listings on a single page
    """
    # Process form submissions
    if request.method == 'POST':
        # Handle Personal Info form
        if 'personal_info_submit' in request.POST:
            instance = None
            if PersonalInfo.objects.exists():
                instance = PersonalInfo.objects.first()
            
            form = PersonalInfoForm(request.POST, request.FILES, instance=instance)
            if form.is_valid():
                form.save()
                messages.success(request, 'Kişisel bilgiler başarıyla kaydedildi.')
                return redirect('cv_app:cv_admin')
            else:
                # Store the form with errors to display later
                personal_info_form = form
        
        # Handle Education form
        elif 'education_submit' in request.POST:
            form = EducationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Eğitim bilgisi başarıyla eklendi.')
                return redirect('cv_app:cv_admin')
            else:
                education_form = form
        
        # Handle Experience form
        elif 'experience_submit' in request.POST:
            form = ExperienceForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'İş deneyimi başarıyla eklendi.')
                return redirect('cv_app:cv_admin')
            else:
                experience_form = form
        
        # Handle Skill form
        elif 'skill_submit' in request.POST:
            form = SkillForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Yetenek başarıyla eklendi.')
                return redirect('cv_app:cv_admin')
            else:
                skill_form = form
        
        # Handle delete operations
        elif 'delete_education' in request.POST:
            education_id = request.POST.get('education_id')
            try:
                education = Education.objects.get(id=education_id)
                education.delete()
                messages.success(request, 'Eğitim bilgisi silindi.')
            except Education.DoesNotExist:
                messages.error(request, 'Eğitim bilgisi bulunamadı.')
            return redirect('cv_app:cv_admin')
        
        elif 'delete_experience' in request.POST:
            experience_id = request.POST.get('experience_id')
            try:
                experience = Experience.objects.get(id=experience_id)
                experience.delete()
                messages.success(request, 'İş deneyimi silindi.')
            except Experience.DoesNotExist:
                messages.error(request, 'İş deneyimi bulunamadı.')
            return redirect('cv_app:cv_admin')
        
        elif 'delete_skill' in request.POST:
            skill_id = request.POST.get('skill_id')
            try:
                skill = Skill.objects.get(id=skill_id)
                skill.delete()
                messages.success(request, 'Yetenek silindi.')
            except Skill.DoesNotExist:
                messages.error(request, 'Yetenek bulunamadı.')
            return redirect('cv_app:cv_admin')
    
    # Initialize forms for GET requests
    # For PersonalInfo, try to get existing instance or create empty form
    personal_info_instance = None
    if PersonalInfo.objects.exists():
        personal_info_instance = PersonalInfo.objects.first()
    
    # Define initial form instances
    if not 'personal_info_form' in locals():
        personal_info_form = PersonalInfoForm(instance=personal_info_instance)
    
    if not 'education_form' in locals():
        education_form = EducationForm()
    
    if not 'experience_form' in locals():
        experience_form = ExperienceForm()
    
    if not 'skill_form' in locals():
        skill_form = SkillForm()
    
    # Get existing data
    educations = Education.objects.all().order_by('-start_date')
    experiences = Experience.objects.all().order_by('-start_date')
    skills = Skill.objects.all().order_by('category', '-level')
    
    # Group skills by category
    skill_categories = {}
    for skill in skills:
        category = skill.category or 'Genel'
        if category not in skill_categories:
            skill_categories[category] = []
        skill_categories[category].append(skill)
    
    # Context for the template
    context = {
        'title': 'CV Yönetim Paneli',
        'personal_info_form': personal_info_form,
        'education_form': education_form,
        'experience_form': experience_form,
        'skill_form': skill_form,
        'educations': educations,
        'experiences': experiences,
        'skill_categories': skill_categories,
        'has_personal_info': personal_info_instance is not None,
    }
    
    return render(request, 'cv_app/cv_admin.html', context)
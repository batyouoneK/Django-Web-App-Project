from django.shortcuts import render
from .models import PersonalInfo, Education, Experience, Skill

def home(request):
    """CV web sitesinin ana sayfası için görünüm fonksiyonu"""
    # Modellerden CV verilerini al
    personal_info = PersonalInfo.objects.first()  # Sadece bir tane kişisel bilgi kaydı olduğunu varsay
    education = Education.objects.all()
    experience = Experience.objects.all()
    skills = Skill.objects.all()
    
    # Şablona aktarılacak içerik sözlüğü
    context = {
        'personal_info': personal_info,
        'education': education,
        'experience': experience,
        'skills': skills,
    }
    
    # CV şablonunu verilerle oluştur
    return render(request, 'cv_app/home.html', context)

def contact(request):
    """İletişim sayfası için görünüm fonksiyonu"""
    # Sadece iletişim bilgilerini içeren kişisel bilgileri al
    personal_info = PersonalInfo.objects.first()
    
    # Şablona aktarılacak içerik sözlüğü
    context = {
        'personal_info': personal_info,
    }
    
    # İletişim şablonunu verilerle oluştur
    return render(request, 'cv_app/contact.html', context)
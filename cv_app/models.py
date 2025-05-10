from django.db import models

class PersonalInfo(models.Model):
    """Model to store basic personal information for the CV"""
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    summary = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Personal Information"
    
    def __str__(self):
        return self.name


class Education(models.Model):
    """Model to store educational background"""
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-end_date', '-start_date']
        verbose_name_plural = "Education"
    
    def __str__(self):
        return f"{self.degree} at {self.institution}"


class Experience(models.Model):
    """Model to store work experience"""
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    
    class Meta:
        ordering = ['-end_date', '-start_date']
    
    def __str__(self):
        return f"{self.position} at {self.company}"


class Skill(models.Model):
    """Model to store skills"""
    name = models.CharField(max_length=50)
    level = models.IntegerField(
        choices=[(1, 'Beginner'), (2, 'Intermediate'), (3, 'Advanced'), (4, 'Expert')],
        default=2
    )
    category = models.CharField(max_length=50, blank=True)
    
    class Meta:
        ordering = ['category', '-level', 'name']
    
    def __str__(self):
        return self.name
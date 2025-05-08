from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import PersonalInfo, Education, WorkExperience, Skill, Project, Certification


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    """Admin configuration for PersonalInfo model."""
    list_display = ('full_name', 'title', 'email', 'updated_at')
    search_fields = ('full_name', 'title', 'email', 'summary')
    fieldsets = (
        (_('Basic Information'), {
            'fields': ('full_name', 'title', 'profile_image', 'summary')
        }),
        (_('Contact Information'), {
            'fields': ('email', 'phone', 'address')
        }),
        (_('Social Profiles'), {
            'fields': ('linkedin', 'github', 'website')
        }),
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    """Admin configuration for Education model."""
    list_display = ('institution', 'degree', 'field_of_study', 'start_date', 'end_date', 'is_current', 'order')
    list_filter = ('is_current', 'degree')
    search_fields = ('institution', 'degree', 'field_of_study')
    list_editable = ('order', 'is_current')
    fieldsets = (
        (_('Institution Details'), {
            'fields': ('institution', 'location')
        }),
        (_('Degree Details'), {
            'fields': ('degree', 'field_of_study')
        }),
        (_('Timeline'), {
            'fields': ('start_date', 'end_date', 'is_current')
        }),
        (_('Additional Information'), {
            'fields': ('description', 'order')
        }),
    )


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    """Admin configuration for WorkExperience model."""
    list_display = ('company', 'position', 'start_date', 'end_date', 'is_current', 'order')
    list_filter = ('is_current', 'company')
    search_fields = ('company', 'position', 'description')
    list_editable = ('order', 'is_current')
    fieldsets = (
        (_('Company Details'), {
            'fields': ('company', 'location')
        }),
        (_('Position Details'), {
            'fields': ('position',)
        }),
        (_('Timeline'), {
            'fields': ('start_date', 'end_date', 'is_current')
        }),
        (_('Additional Information'), {
            'fields': ('description', 'order')
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Admin configuration for Skill model."""
    list_display = ('name', 'category', 'proficiency', 'order')
    list_filter = ('category',)
    search_fields = ('name',)
    list_editable = ('category', 'proficiency', 'order')
    fieldsets = (
        (_('Skill Details'), {
            'fields': ('name', 'category', 'proficiency')
        }),
        (_('Display Options'), {
            'fields': ('order',)
        }),
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Admin configuration for Project model."""
    list_display = ('title', 'start_date', 'end_date', 'is_featured', 'order')
    list_filter = ('is_featured',)
    search_fields = ('title', 'description', 'technologies')
    list_editable = ('is_featured', 'order')
    fieldsets = (
        (_('Project Details'), {
            'fields': ('title', 'description', 'image')
        }),
        (_('Technical Details'), {
            'fields': ('technologies', 'project_url', 'source_code_url')
        }),
        (_('Timeline'), {
            'fields': ('start_date', 'end_date')
        }),
        (_('Display Options'), {
            'fields': ('is_featured', 'order')
        }),
    )


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    """Admin configuration for Certification model."""
    list_display = ('name', 'issuing_organization', 'issue_date', 'expiration_date', 'order')
    list_filter = ('issuing_organization',)
    search_fields = ('name', 'issuing_organization', 'credential_id')
    list_editable = ('order',)
    fieldsets = (
        (_('Certification Details'), {
            'fields': ('name', 'issuing_organization', 'description')
        }),
        (_('Credential Information'), {
            'fields': ('credential_id', 'credential_url')
        }),
        (_('Timeline'), {
            'fields': ('issue_date', 'expiration_date')
        }),
        (_('Display Options'), {
            'fields': ('order',)
        }),
    )
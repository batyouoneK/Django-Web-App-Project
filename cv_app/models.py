from django.db import models
from django.utils.translation import gettext_lazy as _

class PersonalInfo(models.Model):
    """
    Model for storing personal information for the CV.
    """
    full_name = models.CharField(_("Full Name"), max_length=100)
    title = models.CharField(_("Professional Title"), max_length=100)
    profile_image = models.ImageField(_("Profile Image"), upload_to="profile_images/", blank=True, null=True)
    summary = models.TextField(_("Professional Summary"))
    email = models.EmailField(_("Email Address"), max_length=100)
    phone = models.CharField(_("Phone Number"), max_length=20, blank=True, null=True)
    address = models.CharField(_("Address"), max_length=255, blank=True, null=True)
    linkedin = models.URLField(_("LinkedIn Profile"), blank=True, null=True)
    github = models.URLField(_("GitHub Profile"), blank=True, null=True)
    website = models.URLField(_("Personal Website"), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Personal Information")
        verbose_name_plural = _("Personal Information")

    def __str__(self):
        return self.full_name


class Education(models.Model):
    """
    Model for storing education information.
    """
    institution = models.CharField(_("Institution Name"), max_length=255)
    degree = models.CharField(_("Degree/Certificate"), max_length=255)
    field_of_study = models.CharField(_("Field of Study"), max_length=255)
    start_date = models.DateField(_("Start Date"))
    end_date = models.DateField(_("End Date"), blank=True, null=True)
    is_current = models.BooleanField(_("Current Education"), default=False)
    description = models.TextField(_("Description"), blank=True, null=True)
    location = models.CharField(_("Location"), max_length=255, blank=True, null=True)
    order = models.PositiveIntegerField(_("Display Order"), default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Education")
        verbose_name_plural = _("Education")
        ordering = ["order", "-start_date"]

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} at {self.institution}"


class WorkExperience(models.Model):
    """
    Model for storing work experience.
    """
    company = models.CharField(_("Company Name"), max_length=255)
    position = models.CharField(_("Position"), max_length=255)
    start_date = models.DateField(_("Start Date"))
    end_date = models.DateField(_("End Date"), blank=True, null=True)
    is_current = models.BooleanField(_("Current Job"), default=False)
    description = models.TextField(_("Description"))
    location = models.CharField(_("Location"), max_length=255, blank=True, null=True)
    order = models.PositiveIntegerField(_("Display Order"), default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Work Experience")
        verbose_name_plural = _("Work Experience")
        ordering = ["order", "-start_date"]

    def __str__(self):
        return f"{self.position} at {self.company}"


class Skill(models.Model):
    """
    Model for storing skills.
    """
    SKILL_CATEGORY_CHOICES = [
        ('technical', _('Technical')),
        ('soft', _('Soft')),
        ('language', _('Language')),
        ('other', _('Other')),
    ]

    name = models.CharField(_("Skill Name"), max_length=100)
    category = models.CharField(_("Skill Category"), max_length=20, choices=SKILL_CATEGORY_CHOICES, default='technical')
    proficiency = models.PositiveSmallIntegerField(_("Proficiency (1-100)"), default=80, help_text=_("Skill proficiency from 1 to 100"))
    order = models.PositiveIntegerField(_("Display Order"), default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Skill")
        verbose_name_plural = _("Skills")
        ordering = ["category", "order"]

    def __str__(self):
        return self.name


class Project(models.Model):
    """
    Model for storing projects.
    """
    title = models.CharField(_("Project Title"), max_length=255)
    description = models.TextField(_("Description"))
    image = models.ImageField(_("Project Image"), upload_to="project_images/", blank=True, null=True)
    technologies = models.TextField(_("Technologies Used"), blank=True, null=True)
    project_url = models.URLField(_("Project URL"), blank=True, null=True)
    source_code_url = models.URLField(_("Source Code URL"), blank=True, null=True)
    start_date = models.DateField(_("Start Date"), blank=True, null=True)
    end_date = models.DateField(_("End Date"), blank=True, null=True)
    is_featured = models.BooleanField(_("Featured Project"), default=False)
    order = models.PositiveIntegerField(_("Display Order"), default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
        ordering = ["order", "-start_date"]

    def __str__(self):
        return self.title


class Certification(models.Model):
    """
    Model for storing certifications.
    """
    name = models.CharField(_("Certification Name"), max_length=255)
    issuing_organization = models.CharField(_("Issuing Organization"), max_length=255)
    issue_date = models.DateField(_("Issue Date"))
    expiration_date = models.DateField(_("Expiration Date"), blank=True, null=True)
    credential_id = models.CharField(_("Credential ID"), max_length=255, blank=True, null=True)
    credential_url = models.URLField(_("Credential URL"), blank=True, null=True)
    description = models.TextField(_("Description"), blank=True, null=True)
    order = models.PositiveIntegerField(_("Display Order"), default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Certification")
        verbose_name_plural = _("Certifications")
        ordering = ["order", "-issue_date"]

    def __str__(self):
        return f"{self.name} from {self.issuing_organization}"
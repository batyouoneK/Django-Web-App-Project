from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import PersonalInfo, Education, Experience, Skill

# Özel admin sitesi başlığı ve başlık çubuğu
admin.site.site_header = 'CV Web App Admin'
admin.site.site_title = 'CV Web App Admin'
admin.site.index_title = 'CV Yönetim Paneli'

# Geliştirilmiş tek sayfa admin bağlantısı
def cv_admin_link(request):
    url = reverse('cv_app:cv_admin')
    return format_html(
        '<div style="margin: 20px 0; text-align: center;">'
        '<a href="{}" class="button" style="padding: 10px 15px; '
        'background-color: #417690; color: white; text-decoration: none; '
        'border-radius: 4px; font-weight: bold; font-size: 16px;">'
        'Gelişmiş CV Yönetim Paneli (Tüm İşlemler Tek Sayfada)</a></div>',
        url
    )

# Admin ana sayfasına bağlantı ekle
admin.site.index_template = 'admin/custom_index.html'

# Tek sayfa CV admin paneline bağlantı eklemek için Mixin
class CVAdminLinkMixin:
    def cv_admin_button(self, obj=None):
        url = reverse('cv_app:cv_admin')
        return format_html(
            '<a href="{}" class="button" style="background-color: #417690; '
            'color: white; text-decoration: none; padding: 5px 10px; '
            'border-radius: 4px; display: inline-block; margin-top: 5px;">'
            'Tek Sayfa CV Paneli</a>',
            url
        )
    cv_admin_button.short_description = 'Tek Sayfa CV Paneli'

@admin.register(PersonalInfo)
class PersonalInfoAdmin(CVAdminLinkMixin, admin.ModelAdmin):
    list_display = ('name', 'title', 'email', 'phone', 'cv_admin_button')
    search_fields = ('name', 'email')
    readonly_fields = ('cv_admin_button',)


@admin.register(Education)
class EducationAdmin(CVAdminLinkMixin, admin.ModelAdmin):
    list_display = ('institution', 'degree', 'field_of_study', 'start_date', 'end_date', 'is_current', 'cv_admin_button')
    list_filter = ('is_current',)
    search_fields = ('institution', 'degree', 'field_of_study')
    list_display_links = ('institution', 'degree')
    readonly_fields = ('cv_admin_button',)


@admin.register(Experience)
class ExperienceAdmin(CVAdminLinkMixin, admin.ModelAdmin):
    list_display = ('company', 'position', 'start_date', 'end_date', 'is_current', 'cv_admin_button')
    list_filter = ('is_current',)
    search_fields = ('company', 'position')
    list_display_links = ('company', 'position')
    readonly_fields = ('cv_admin_button',)


@admin.register(Skill)
class SkillAdmin(CVAdminLinkMixin, admin.ModelAdmin):
    list_display = ('name', 'level', 'category', 'cv_admin_button')
    list_filter = ('level', 'category')
    search_fields = ('name', 'category')
    readonly_fields = ('cv_admin_button',)
from django.contrib import admin
from .models import Person, Works, Studies, Certificate


class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'my_email']


class WorksAdmin(admin.ModelAdmin):
    list_display = ['name']


class StudiesAdmin(admin.ModelAdmin):
    list_display = ['name']


class CertificateAdmin(admin.ModelAdmin):
    list_display = ['course', 'place_sturies']

# Register your models here.

admin.site.register(Person, PersonAdmin)
admin.site.register(Works, WorksAdmin)
admin.site.register(Studies, StudiesAdmin)
admin.site.register(Certificate, CertificateAdmin)

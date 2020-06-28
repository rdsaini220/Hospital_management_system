from django.contrib import admin
from home.models import Doctor,Patient,Appointment

# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name', 'mobile','spacial',]
    list_filter = ('spacial',)

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient)
admin.site.register(Appointment)
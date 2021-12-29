from django.contrib import admin
from .models import Person, Employee


class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'country')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name',)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Person, PersonAdmin)

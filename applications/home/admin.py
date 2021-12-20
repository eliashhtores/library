from django.contrib import admin
from .models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'country')


admin.site.register(Person, PersonAdmin)

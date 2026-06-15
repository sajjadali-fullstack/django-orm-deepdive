from django.contrib import admin
from testapp.models import Prisoner


class PrisonerAdmin(admin.ModelAdmin):
    list_display = ['id', 'prisoner_id', 'first_name', 'last_name','gender', 'crimes', 'arrest_date', 'arresting_officer', 'status']
    list_filter = ['status']    
    search_fields = ['prisoner_id', 'first_name', 'last_name', 'crimes', 'arresting_officer']

# Register your models here.
admin.site.register(Prisoner, PrisonerAdmin)
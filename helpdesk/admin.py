from django.contrib import admin
from helpdesk.models import help 
# Register your models here.
class help_admin(admin.ModelAdmin):
    list_display=('name','concern')
admin.site.register(help,help_admin)

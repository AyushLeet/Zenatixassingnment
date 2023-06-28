from django.contrib import admin
from api.models import Event,User
# Register your models here..

class EventAdmin(admin.ModelAdmin):
    list_display=('name','location','type')
    search_fields=('name',)   
    
class UserAdmin(admin.ModelAdmin):
    list_display=('name','email','event')
    list_filter=('event',)

admin.site.register(Event,EventAdmin)
admin.site.register(User,UserAdmin)

from django.contrib import admin

from crudapp.models import Core

# Register your models here.

# admin.site.register(Core) 

@admin.register(Core)
class PostAdmin(admin.ModelAdmin):
    prepopulate_fields = {'slug': ('title',),}
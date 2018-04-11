from django.contrib import admin
from .models import Blank

class BlankAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'base', 'doc', 'pdf')
    list_filter = ('title',)

admin.site.register(Blank, BlankAdmin)
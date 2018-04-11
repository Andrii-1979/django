from django.contrib import admin
from .models import Belt

class BeltAdmin(admin.ModelAdmin):
    list_display = ('department', 'tipe', 'number', 'data')
    list_filter = ('department','tipe')

admin.site.register(Belt, BeltAdmin)
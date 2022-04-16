from django.contrib import admin
from .models import Lugat

@admin.register(Lugat)
class LugatAdmin(admin.ModelAdmin):
    list_display = ['inglizcha', 'uzbekcha']



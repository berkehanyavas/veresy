from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Hareket)
class HareketAdmin(admin.ModelAdmin):
    list_display = [
        'yazar',
        'hedef',
        'durum',
        'miktar'
    ]
    
    list_filter = [
        'yazar',
        'hedef',
        'durum',
        'miktar'
    ]
    
    class Meta:
        model = Hareket
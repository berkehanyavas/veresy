from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Kisi)
class KisiAdmin(admin.ModelAdmin):
    list_display = [
        'isim',
        'yazar'
    ]

    list_filter = [
        'yazar'
    ]

    class Meta:
        model = Kisi
                
# @admin.register(Firma)
# class FirmaAdmin(admin.ModelAdmin):
#     list_display = [
#         'isim',
#         'yazar'
#     ]
    
#     list_filter = [
#         'yazar'
#     ]
    
#     class Meta:
#         model = Firma

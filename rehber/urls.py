from django.urls import path
from . import views

app_name = 'rehber'

urlpatterns = [
    path('',views.index, name='rehberindex'),
    path('ekle/',views.ekle,name='kisiekle'),
    path('kisi/<int:id>',views.detay,name='detay'),
    path('kisi/guncelle/<int:id>',views.guncelle,name='guncelle'),
    path('kisi/sil/<int:id>',views.sil,name='sil'),
    
]
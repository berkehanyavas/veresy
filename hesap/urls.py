from django.urls import path
from . import views

app_name = 'hesap'

urlpatterns = [
    path('ekle/<int:id>',views.ekle,name='ekle'),
    path('sil/<int:id>',views.sil,name='sil'),
    path('duzenle/<int:id>',views.guncelle,name='guncelle'),
    path('goruntule/<int:id>',views.goruntule,name='goruntule')
    
]
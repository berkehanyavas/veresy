from django.db import models
from rehber.models import Kisi
from ckeditor.fields import RichTextField
import datetime

# Create your models here.

class Hareket(models.Model):
    yazar = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    hedef = models.ForeignKey(Kisi,on_delete=models.CASCADE)
    miktar = models.FloatField(verbose_name='Miktar')
    SECENEK = (
        ('Alindi','Alindi'),
        ('Alinacak','Alinacak')
    )
    durum = models.CharField(max_length=50,choices=SECENEK,default=SECENEK[1],verbose_name='Durum')
    aciklama = RichTextField(blank=True,null=True)
    tarih = models.DateField(verbose_name='Tarih',blank=True,null=True)
    
    def __str__(self):
        return self.yazar.username

    
    def save(self, *args, **kwargs):
        if self.tarih is None:
            self.tarih = datetime.datetime.now()
        super().save(*args, **kwargs)
        
class Sil(models.Model):
    flag = models.BooleanField('Emin misiniz?')
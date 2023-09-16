from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


# class Firma(models.Model):
#     yazar = models.ForeignKey('auth.User',on_delete=models.CASCADE)
#     isim = models.CharField(max_length=20)
    
#     def __str__(self):
#         return self.isim

    # eklenebilir
    
class Kisi(models.Model):
    yazar = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    isim = models.CharField(max_length=30)
    # firma = models.ForeignKey(Firma,related_name='Firma',blank=True,null=True,on_delete=models.CASCADE)
    tel1 = models.CharField(max_length=444,blank=True,null=True)
    tel2 = models.CharField(max_length=444,blank=True,null=True)
    adres = RichTextField(blank=True,null=True)
    notlar = RichTextField(blank=True,null=True)

    def __str__(self):
        return self.isim
    
    # eklenebilir
    
class Sil(models.Model):
    flag = models.BooleanField('Emin misiniz?')
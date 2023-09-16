from django import forms
from .models import Hareket, Sil

class HareketForm(forms.ModelForm):
    class Meta:
        model = Hareket
        fields = [
            'miktar',
            'durum',
            'aciklama',
            'tarih'
        ]
        
class SilForm(forms.ModelForm):
    class Meta:
        model = Sil
        fields = [
            'flag'
        ]
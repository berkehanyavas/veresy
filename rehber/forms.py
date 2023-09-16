from django import forms
from .models import Kisi, Sil

class KisiForm(forms.ModelForm):
    class Meta:
        model = Kisi
        fields = [
            'isim',
            # 'firma',
            'tel1',
            'tel2',
            'adres',
            'notlar'
        ]
        
class SilForm(forms.ModelForm):
    class Meta:
        model = Sil
        fields = [
            'flag'
        ]
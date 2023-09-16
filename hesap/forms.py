from django import forms
from .models import Hareket, Sil

class DateInput(forms.DateInput):
    input_type = 'date'

class HareketForm(forms.ModelForm):
    class Meta:
        model = Hareket
        fields = [
            'miktar',
            'durum',
            'aciklama',
            'tarih'
        ]
        widgets = {
            'tarih': DateInput(),
        }
        
class SilForm(forms.ModelForm):
    class Meta:
        model = Sil
        fields = [
            'flag'
        ]
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Kullanici Adi')
    password = forms.CharField(label='Parola',widget=forms.PasswordInput)
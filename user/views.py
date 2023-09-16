from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def loginUser(request):
    if request.user.is_authenticated:
        messages.warning(request,'Cikis yapmadan bu sayfayi goremezsiniz.')
        return redirect('index')

    form = LoginForm(request.POST or None)
    context = {
        'sayfaadi': 'Giris Yap',
        'form': form
    }
    
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        
        user = authenticate(username=username,password=password)
        
        if user is None:
            messages.warning(request,'Kullanici adi veya parola hatali.')
            return redirect('login')
        
        messages.success(request,'Basariyla giris yapildi.')
        login(request,user)

        return redirect('index')
    return render(request,'login.html',context)


def logoutUser(request):
    if not request.user.is_authenticated:
        # messages.warning(request,'Giris yapmadan bu sayfayi goremezsiniz.')
        return redirect('login')

    logout(request)
    messages.success(request,'Basariyla cikis yaptiniz.')
    return redirect('index')
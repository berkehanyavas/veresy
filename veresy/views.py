from django.shortcuts import render, redirect
from django.contrib import messages
from hesap.models import Hareket

def index(request):
    if not request.user.is_authenticated:
        messages.warning(request,'Giris yapmadan bu sayfayi goremezsiniz.')
        return redirect('/user/login')
    
    hareketler = reversed(Hareket.objects.filter(yazar = request.user))
    
    # reversed(hareketler)

    context = {
        'sayfaadi': 'Anasayfa',
        'hareketler': hareketler
    }
    return render(request,'index.html',context)

#anasayfada son hareketleri goster

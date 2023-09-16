from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import HareketForm, SilForm
from .models import Hareket
from rehber.models import Kisi
import datetime



# Create your views here.


    

def ekle(request,id):
    if not request.user.is_authenticated:
        messages.warning(request,'Giris yapmadan bu sayfayi goremezsiniz.')
        return redirect('/user/login')

    form = HareketForm(request.POST or None)
    kisi = Kisi.objects.filter(id=id).first()
    # print(kisi.total)
    if form.is_valid():
        islem = form.save(commit=False)
        islem.yazar = request.user
        islem.hedef = kisi
        islem.save()
        

        kisi.son_islem = datetime.datetime.today()
        kisi.son_miktar = islem.miktar
        kisi.save()
        messages.success(request,'Islem basariyla gerceklestirildi.')
        # print(islem.hedef.id) #formda girilen hedef
        # print(islem.miktar) #formda girilen miktar
        # print(islem.durum)
        
        
        
        
        return redirect(f'/rehber/kisi/{id}')
    
    context = {
        'sayfaadi': 'Islem Ekle',
        'form': form
    }
    return render(request,'ekle.html',context)

def guncelle(request,id):
    if not request.user.is_authenticated:
        messages.warning(request,'Giris yapmadan bu sayfayi goremezsiniz.')
        return redirect('/user/login')

    hareket = get_object_or_404(Hareket,id=id)
    if hareket.yazar != request.user:
        messages.error(request,'Bu isleme yetkiniz bulunmamaktadir!')
        return redirect('index')
    form = HareketForm(request.POST or None, request.FILES or None,instance=hareket)
    if form.is_valid():
        hareket = form.save(commit=False)
        hareket.yazar = request.user
        hareket.save()
        
        messages.success(request,'Islem basariyla gerceklestirildi.')
        return redirect(f'/hesap/goruntule/{hareket.id}')
    
    context = {
        'sayfaadi':'Islem Guncelle',
        'form': form,
        'id':hareket.id,
        'flag': 'hesap'
    }
    
    return render(request,'ekle.html',context)

def sil(request,id):
    if not request.user.is_authenticated:
        messages.warning(request,'Giris yapmadan bu sayfayi goremezsiniz.')
        return redirect('/user/login')

    hareket = get_object_or_404(Hareket,id=id)
    if hareket.yazar != request.user:
        messages.error(request,'Bu isleme yetkiniz bulunmamaktadir!')
        return redirect('index')
    form = SilForm(request.POST or None)
    if form.is_valid():
        sure = form.save(commit=False)
        if sure.flag == True:
            hareket.delete()
            messages.success(request,'Islem basariyla gerceklestirildi.')
            return redirect(f'/rehber/kisi/{hareket.hedef.id}')
        else:
            messages.warning(request,'Islem iptal edildi.')
            return redirect(f'/hesap/duzenle/{hareket.id}')
    context = {
        'sayfaadi': 'Islem Sil',
        'form':form
    }
    
    return render(request,'ekle.html',context)

def goruntule(request,id):
    if not request.user.is_authenticated:
        messages.warning(request,'Giris yapmadan bu sayfayi goremezsiniz.')
        return redirect('/user/login')

    hareket = get_object_or_404(Hareket,id=id)
    if hareket.yazar != request.user:
        messages.error(request,'Bu isleme yetkiniz bulunmamaktadir!')
        return redirect('index')

    context = {
        'sayfaadi': 'Islem Goruntule',
        'hareket': hareket
    }
    
    return render(request,'hareket.html',context)
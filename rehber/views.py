from django.shortcuts import render,redirect
from django.contrib import messages
from hesap.models import Hareket
from .models import Kisi
from .forms import KisiForm, SilForm

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        messages.warning(request,'Giris yapmadan bu sayfayi goremezsiniz.')
        return redirect('/user/login')
    
    contact = Kisi.objects.filter(yazar = request.user)
    total = []
    sontarih = []
    sonmiktar = []
    
    for i in contact:
        toplam = Hareket.objects.filter(yazar = request.user, hedef = i)
        a = 0
        for j in toplam:
            if j.durum == 'Alinacak':
                a = a - j.miktar
            else:
                a = a + j.miktar
        total.append(a)
    for i in contact:
        h = Hareket.objects.filter(yazar = request.user, hedef = i).order_by('-tarih').first()
        if h != None:
            sontarih.append(h.tarih)
            sonmiktar.append(h.miktar)
        else:
            sontarih.append(None)
            sonmiktar.append(None)
    
    context = {
        'sayfaadi': 'Rehber',
        'kisiler': zip(contact,total,sontarih,sonmiktar)
        # 'toplamlar': total,
    }
    return render(request,'rehber.html',context)

def ekle(request):
    if not request.user.is_authenticated:
        messages.warning(request,'Giris yapmadan bu sayfayi goremezsiniz.')
        return redirect('/user/login')

    form = KisiForm(request.POST or None)
    
    if form.is_valid():
        islem = form.save(commit=False)
        islem.yazar = request.user
        islem.save()
        messages.success(request,'Rehberinize basariyla eklendi.')
        return redirect('/rehber')
    
    context = {
        'sayfaadi': 'Kisi Ekle',
        'form': form
    }
    
    return render(request,'ekle.html',context)

def guncelle(request,id):
    if not request.user.is_authenticated:
        messages.warning(request,'Giris yapmadan bu sayfayi goremezsiniz.')
        return redirect('/user/login')

    kisi = Kisi.objects.filter(yazar = request.user,id=id).first()
    if kisi.yazar != request.user:
        messages.warning(request,'Bu isleme yetkiniz bulunmamaktadir.')
        return redirect('index')
    form = KisiForm(request.POST or None,instance=kisi)
    if form.is_valid():
        islem = form.save(commit=False)
        islem.yazar = request.user
        islem.save()
        messages.success(request,'Islem basariyla gerceklestirildi.')
        return redirect('index')
    
    context = {
        'sayfaadi': 'Kisi Guncelle',
        'form': form,
        'flag': 'rehber',
        'id':kisi.id
    }
    return render(request,'ekle.html',context)

def detay(request,id):
    if not request.user.is_authenticated:
        messages.warning(request,'Giris yapmadan bu sayfayi goremezsiniz.')
        return redirect('/user/login')
    
    
    kisi = Kisi.objects.filter(id=id).first()
    
    if kisi.yazar != request.user:
        messages.warning(request,'Bu sayfayi goruntuleme yetkiniz bulunmamaktadir!')
        return redirect('/rehber')
    
    hareketler = Hareket.objects.filter(hedef=kisi,yazar=request.user).order_by('-tarih')
    # hareketler = hareketler.reverse()
    
    a = 0

    for i in hareketler:
        if i.durum == 'Alinacak':
            a += i.miktar
        else:
            a -= i.miktar
    
    context = {
        'sayfaadi': kisi,
        'kisi': kisi,
        'hareketler': hareketler,
        "total": a
    }
    
    return render(request,'detay.html',context)

def sil(request,id):
    if not request.user.is_authenticated:
        messages.warning(request,'Giris yapmadan bu sayfayi goremezsiniz.')
        return redirect('/user/login')

    kisi = Kisi.objects.filter(id = id).first()
    if kisi.yazar != request.user:
        messages.error(request,'Bu isleme yetkiniz bulunmamaktadir!')
        return redirect('/rehber')
    
    form = SilForm(request.POST or None)
    if form.is_valid():
        sure = form.save(commit=False)
        if sure.flag == True:
            kisi.delete()
            messages.success(request,'Islem basariyla gerceklestirildi.')
        else:
            messages.warning(request,'Islem iptal edildi.')
        return redirect('/rehber')
    
    context = {
        'sayfaadi': 'Kisi Sil',
        'form': form
    }
    
    return render(request,'ekle.html',context)
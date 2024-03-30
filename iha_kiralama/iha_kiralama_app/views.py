
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import * 
from rest_framework import status

@api_view(['GET'])
def anasayfa(request):
    return render(request, 'iha_kiralama/templates/anasayfa.html')

@api_view(['GET'])
def iha_detaylar(request, iha_id):
    iha = get_object_or_404(IHA, pk=iha_id)
    serializer = IHASerializer(iha)
    return render(request, 'iha_kiralama/templates/iha_detaylar.html', {'iha': serializer.data})

@api_view(['GET'])
def ihalarim_detaylar(request, iha_id):
    ihalarim = get_object_or_404(Ihalarim, pk=iha_id)
    serializer = IhalarimSerializer(ihalarim)
    return render(request, 'iha_kiralama/templates/iha_detaylar.html', {'iha': serializer.data})

@api_view(['POST'])
def ihayi_sil(request, iha_id):
    iha = get_object_or_404(Ihalarim, pk=iha_id)
    iha.delete()
    return redirect('ihalarim')

@api_view(['POST'])
def ihayi_duzenle(request, iha_id):
    iha = get_object_or_404(Ihalarim, pk=iha_id)
    # Serializer ile kısmi güncelleme yapma
    serializer = IhalarimSerializer(iha, data=request.data, partial=True)
    # Serializer'ın doğruluğunu kontrol et
    if serializer.is_valid():
        # Serializer ile veriyi güncelle
        serializer.save()
        # İhalarım sayfasına yönlendir
        return redirect('ihalarim')
    # Hatalı veri durumunda hata mesajlarını döndür
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'GET'])
def iha_ekle(request):
    if request.method == 'POST':
        form = IHAForm(request.POST)
        if form.is_valid():
            iha = form.save(commit=False)
            iha.olusturan = request.user
            iha.save()
            return redirect('iha_listele')
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        form = IHAForm()
        return render(request, 'iha_kiralama/templates/iha_islemleri.html', {'form': form})


@api_view(['GET'])
def ihalarim(request):
    ihalar = Ihalarim.objects.filter(olusturan=request.user)
    serializer = IhalarimSerializer(ihalar, many=True)
    return render(request, 'iha_kiralama/templates/ihalarim.html', {'ihalar': serializer.data})

@api_view(['POST', 'GET']) #gerek var mı
def cikis_yap(request):
    logout(request)
    return redirect('anasayfa')

@api_view(['POST', 'GET'])
def uye_ol(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('anasayfa')  # Üye olunduktan sonra ana sayfaya yönlendir
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        form = UserRegisterForm()
    return render(request, 'iha_kiralama/templates/uye_ol.html', {'form': form})

@api_view(['POST', 'GET'])
def giris(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('anasayfa')  # Giriş yapıldıktan sonra ana sayfaya yönlendir
            else:
                return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        form = UserLoginForm()
    return render(request, 'iha_kiralama/templates/giris.html', {'form': form})

@api_view(['GET'])
@login_required
def kiralanan_ihalar(request):
    kiralanan_ihalar = KiralananIHA.objects.filter(kiralayan_uye=request.user.id)
    serializer = KiralananIHASerializer(kiralanan_ihalar, many=True)
    return render(request, 'iha_kiralama/templates/kiralanan_ihalar.html', {'kiralanan_ihalar': serializer.data})


@api_view(['GET'])
def iha_listele(request):
    iha_list = IHA.objects.all().order_by('id')
    benim_iha = Ihalarim.objects.all().order_by('id')
    serializer_iha_list = IHASerializer(iha_list, many=True)
    serializer_benim_iha = IHAlarimSerializer(benim_iha, many=True)
    return render(request, 'iha_kiralama/templates/iha_listele.html', {'iha_list': serializer_iha_list.data,'benim_iha': serializer_benim_iha.data  })

@api_view(['POST'])
@login_required
def kiralama_islemi(request, iha_id):
    if request.method == 'POST':
        baslangic_tarihi = request.data.get('baslangicTarihi')
        bitis_tarihi = request.data.get('bitisTarihi')
        user = request.user
        iha = get_object_or_404(IHA, pk=iha_id)
        kiralanan_iha = KiralananIHA.objects.create(kiralayan_uye=user, iha=iha,
                                                    baslangic_tarihi=baslangic_tarihi, bitis_tarihi=bitis_tarihi)
        messages.success(request, 'IHA başarıyla kiralandı!')
        return redirect('kiralanan_ihalar')
    else:
        # POST dışındaki istekler için anasayfaya yönlendir
        return redirect('anasayfa')

@api_view(['GET'])
@login_required
def profile(request):
    user = request.user
    return render(request,'iha_kiralama/templates/profil.html', {'user': user})

@api_view([ 'POST'])
@login_required
def kiralama_sil(request, kiralanan_iha_id):
    try:
        kiralanan_iha = KiralananIHA.objects.get(id=kiralanan_iha_id)
    except KiralananIHA.DoesNotExist:
        return Response({"message": "Kiralanan IHA bulunamadı."}, status=status.HTTP_404_NOT_FOUND)

    if kiralanan_iha.kiralayan_uye.id != request.user.id:
        return Response({"message": "Bu işlemi gerçekleştirmek için yetkiniz yok."}, status=status.HTTP_403_FORBIDDEN)
    kiralanan_iha.delete()
    return redirect('kiralanan_ihalar')



    
@api_view(['POST'])
@login_required
def tarih_duzenle(request, kiralanan_iha_id):
    if request.method == 'POST':
        baslangic_tarihi = request.POST.get('baslangicTarihi')
        bitis_tarihi = request.POST.get('bitisTarihi')

        # Kiralanan IHA'yı güncelle
        kiralanan_iha = KiralananIHA.objects.get(id=kiralanan_iha_id)
        serializer = KiralananIHASerializer(kiralanan_iha, data=request.data, partial=True)
        if serializer.is_valid():
          kiralanan_iha.baslangic_tarihi = baslangic_tarihi
          kiralanan_iha.bitis_tarihi = bitis_tarihi
          serializer.save()
        # Başarılı mesaj göster
          messages.success(request, 'Tarihler başarıyla güncellendi!')

        # Kiralanan IHAlar sayfasına yönlendir
        return redirect('kiralanan_ihalar')
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




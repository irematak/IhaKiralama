
from django.urls import path
from iha_kiralama_app import views


urlpatterns = [
    path('', views.anasayfa, name='anasayfa'), # Anasayfa URL'si
    path('giris_yap/', views.giris, name='giris'), # Anasayfa URL'si
    path('cikis_yap/', views.cikis_yap, name='cikis_yap'), # Anasayfa URL'si
    path('uye_ol/', views.uye_ol, name='uye_ol'), # Anasayfa URL'si
    path('iha_ekle/', views.iha_ekle, name='iha_ekle'),
    path('iha_listele/', views.iha_listele, name='iha_listele'),
    path('iha_detaylar/<int:iha_id>/', views.iha_detaylar, name='iha_detaylar'),
    path('ihalarim_detaylar/<int:iha_id>/', views.ihalarim_detaylar, name='ihalarim_detaylar'),
    path('kiralama_islemi/<int:iha_id>/', views.kiralama_islemi, name='kiralama_islemi'),
    path('profil/', views.profile, name='profile'),
    path('kiralanan_ihalar/', views.kiralanan_ihalar, name='kiralanan_ihalar'),
    path('kiralama_sil/<int:kiralanan_iha_id>/', views.kiralama_sil, name='kiralama_sil'),
    path('tarih_duzenle/<int:kiralanan_iha_id>/', views.tarih_duzenle, name='tarih_duzenle'),
    path('ihalarim/', views.ihalarim, name='ihalarim'),
    path('ihayi_sil/<int:iha_id>/', views.ihayi_sil, name='ihayi_sil'),
    path('ihalarim/<int:iha_id>/duzenle/', views.ihayi_duzenle, name='ihayi_duzenle'),
  
   
]

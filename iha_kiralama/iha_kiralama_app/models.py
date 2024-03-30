from django.db import models
from django.contrib.auth.models import User


      

class IHA(models.Model):
    marka = models.CharField(max_length=100,default="foobar")
    model = models.CharField(max_length=100)
    agirlik = models.FloatField()
    uzunluk = models.FloatField()
    havada_kalıs_suresi = models.FloatField(default= 1)
    
    def __str__(self):
        return self.model

class Ihalarim(models.Model):
    olusturan = models.ForeignKey(User, on_delete=models.CASCADE)
    marka = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    agirlik = models.FloatField()
    uzunluk = models.FloatField()
    havada_kalıs_suresi = models.FloatField()
    
    def __str__(self):
        return self.model



class KiralananIHA(models.Model):
    kiralayan_uye = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)
    iha = models.ForeignKey('IHA', on_delete=models.CASCADE, default=1)
    baslangic_tarihi = models.DateField()
    bitis_tarihi = models.DateField()

    # Gerekirse başka alanlar da ekleyebilirsiniz

    class Meta:
        app_label = 'iha_kiralama_app'

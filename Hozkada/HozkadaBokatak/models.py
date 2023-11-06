from django.db import models

# Create your models here.

class Bezeroa(models.Model):
    NAN = models.CharField(max_length=10)
    izena = models.CharField(max_length=20)
    abizena = models.CharField(max_length=20)
    abizena2 = models.CharField(max_length=20)
    telefonoa = models.CharField(max_length=20)
    emaila = models.EmailField
    helbidea = models.CharField(max_length=100)
    postakodea = models.CharField(max_length=10)
    img = models.ImageField(upload_to='img/erabiltzaileak')

    def __unicode__(self):
        return self.NAN

class Platerra(models.Model): 
    motak = (
        ('haragia', 'Haragia'), 
        ('arraina', 'Arraina'), 
        ('begetarianoa', 'Begetarianoa'), 
        ('beganoa', 'Beganoa'), 
    )
    izena = models.CharField(max_length=100)
    deskribapena = models.CharField(max_length=1000)
    prezioa = models.FloatField(default=0)
    mota = models.CharField(max_length=20, choices=motak, default='haragia')
    img = models.ImageField(upload_to='img/bokatak')

    def __unicode__(self):
        return self.izena

class Eskaera(models.Model):
    id_bezeroa = models.ForeignKey(Bezeroa, on_delete=models.CASCADE)
    eskaera_data = models.DateField
    egoera = models.BooleanField(default=True)

    def __unicode__(self):
        return self.id

class Platerra_Eskaera(models.Model):
    eskaera_id = models.ForeignKey(Eskaera, on_delete=models.CASCADE)
    platerra_id = models.ForeignKey(Platerra, on_delete=models.CASCADE)
    kantitatea = models.IntegerField


class Alergia(models.Model):
    izena = models.CharField(max_length=30)
    img = models.ImageField(upload_to='img/alergiak')

    def __unicode__(self):
        return self.izena

class Deskontua(models.Model):
    izena = models.CharField(max_length=50)
    ehunekoa = models.FloatField
    kantitatea = models.IntegerField

    def __unicode__(self):
        return self.izena


class Deskontua_Platerra(models.Model):
    platerra_id = models.ForeignKey(Platerra, on_delete=models.CASCADE)
    deskontua_id = models.ForeignKey(Deskontua, on_delete=models.CASCADE)

class Alergia_Platerra(models.Model): 
    platerra_id = models.ForeignKey(Platerra, on_delete=models.CASCADE)
    alergia_id = models.ForeignKey(Alergia, on_delete=models.CASCADE)

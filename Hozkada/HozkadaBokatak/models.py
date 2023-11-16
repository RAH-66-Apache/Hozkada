from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Bezeroa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nan = models.CharField(max_length=10)
    izena = models.CharField(max_length=20)
    abizena = models.CharField(max_length=20)
    abizena2 = models.CharField(max_length=20)
    telefonoa = models.CharField(max_length=20)
    emaila = models.EmailField(max_length=50, default='')
    helbidea = models.CharField(max_length=100)
    postakodea = models.CharField(max_length=10)
    bidalketaKostua = models.FloatField(default=0)
    img = models.ImageField(upload_to='img/erabiltzaileak')

    def __str__(self):
        return self.izena

class Platerra(models.Model):
    motak = (
        ('haragia', 'Haragia'),
        ('arraina', 'Arraina'),
        ('begetarianoa', 'Begetarianoa'),
        ('beganoa', 'Beganoa'),
         ('edaria', 'Edaria'),
    )
    izena = models.CharField(max_length=100)
    deskribapena = models.CharField(max_length=1000)
    prezioa = models.FloatField(default=0)
    mota = models.CharField(max_length=20, choices=motak, default='haragia')
    img = models.ImageField(upload_to='img/bokatak')
    alergiak = models.ManyToManyField('Alergia', blank=True)

    def precio_con_descuento(self):
        deskontua_set = self.deskontua_platerra_set.all()
        print("Deskontua_Platerra instances:", deskontua_set)
        deskontua = deskontua_set.first()  # Suponiendo que solo hay un descuento por plato
        if deskontua:
            descuento_porcentaje = deskontua.deskontua_id.ehunekoa
            precio_descuento = self.prezioa - (self.prezioa * descuento_porcentaje / 100)
            return round(precio_descuento, 2)
        else:
            return self.prezioa

    def __str__(self):
        return self.izena

class Eskaera(models.Model):
    id_bezeroa = models.ForeignKey(Bezeroa, on_delete=models.CASCADE)
    eskaera_data = models.DateField(default=timezone.now)
    egoera = models.BooleanField(default=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return f"{self.id} - {self.id_bezeroa}"

class Platerra_Eskaera(models.Model):
    eskaera_id = models.ForeignKey(Eskaera, on_delete=models.CASCADE)
    platerra_id = models.ForeignKey(Platerra, on_delete=models.CASCADE)
    kantitatea = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.eskaera_id} - {self.platerra_id}"

class Alergia(models.Model):
    izena = models.CharField(max_length=30)
    img = models.ImageField()

    def __str__(self):
        return self.izena

class Deskontua(models.Model):
    izena = models.CharField(max_length=50)
    ehunekoa = models.FloatField(default=0)
    kantitatea = models.IntegerField(default=0)

    def __str__(self):
        return self.izena

class Deskontua_Platerra(models.Model):
    platerra_id = models.ForeignKey(Platerra, on_delete=models.CASCADE)
    deskontua_id = models.ForeignKey(Deskontua, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.platerra_id} - {self.deskontua_id}"

class Alergia_Platerra(models.Model):
    platerra_id = models.ForeignKey(Platerra, on_delete=models.CASCADE)
    alergia_id = models.ForeignKey(Alergia, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.alergia_id} - {self.platerra_id}"
from django.db import models
from django.contrib.auth.models import User

# Create your models here.  
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="no-profile.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Data(models.Model):
    kota = models.CharField(max_length=200, null=True)
    kelurusan = models.FloatField()
    elevasi = models.FloatField()
    geologi = models.FloatField()
    jalan = models.FloatField()
    kel = models.FloatField()
    lahan = models.FloatField()
    sungai = models.FloatField()
    tanah = models.FloatField()
    hujan = models.FloatField()
    aspek = models.FloatField()

    def __str__(self):
        return self.kota
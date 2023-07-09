from django.db import models
# Create your models here.

class Person(models.Model):
    p_id = models.AutoField(primary_key = True)
    full_name = models.CharField(max_length=50 , null = True)
    gender =  models.CharField(max_length=10 , null = True)
    address_society = models.CharField(max_length=100 , null= True)
    address_house_no = models.CharField(max_length=100 , null= True)
    mobile_no = models.CharField(max_length =15 , null=True)
    whatsapp_no = models.CharField(max_length=15 , null = True)
    old_karyakar = models.CharField(max_length=100 , null= True)
    karykar = models.CharField(max_length=100 , null= True)
    # family_id = models.IntegerField(default=0)
    # age = models.IntegerField(null=True)

    def __str__(self):
        return str(self.p_id) +" - "+ self.full_name + " - " + self.mobile_no

class date_person(models.Model):
    date_sabha = models.DateField(auto_now_add=True)
    # date_sabha.editable=True
    ref_id = models.ForeignKey("hajri.Person",on_delete=models.DO_NOTHING)

class Family(models.Model):
    family_id = models.IntegerField(primary_key=True)
    family_name = models.CharField(max_length=50)
    family_head = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    details = models.JSONField()
    
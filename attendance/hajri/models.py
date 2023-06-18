from django.db import models
# Create your models here.

class Person(models.Model):
    p_id = models.AutoField(primary_key = True)
    family_id = models.IntegerField(default=0)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    full_name = models.CharField(max_length=50)
    gender =  models.BooleanField(default = True)
    gender_text = models.CharField(max_length=10 , default="male")
    age = models.IntegerField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return str(self.p_id) +"   ---   "+ self.first_name

class date_person(models.Model):
    date_sabha = models.DateField(auto_now_add=True)
    # date_sabha.editable=True
    ref_id = models.ForeignKey("hajri.Person",on_delete=models.DO_NOTHING)

class Family(models.Model):
    family_id = models.IntegerField(primary_key=True)
    family_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)  
from django.db import models
# Create your models here.

class Person(models.Model):
    p_id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    full_name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return str(self.p_id) +"   ---   "+ self.first_name

class date_person(models.Model):
    date_sabha = models.DateField()
    ref_id = models.ForeignKey("hajri.Person",on_delete=models.DO_NOTHING)
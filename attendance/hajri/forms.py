from django.forms import ModelForm
from .models import Person,date_person

class PersonForm(ModelForm):

    class Meta:
        model = Person 
        fields = "__all__"



class date_personForm(ModelForm):

    class Meta:
        model = date_person
        fields = ['ref_id']

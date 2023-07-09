from django.forms import ModelForm
from .models import Family,Sabha_attendance_entry

class FamilyForm(ModelForm):

    class Meta:
        model = Family 
        fields = "__all__"



class form_sabha_attendance_entry(ModelForm):

    class Meta:
        model = Sabha_attendance_entry
        fields = ['family_ref','male_attended','female_attended']

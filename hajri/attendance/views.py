from django.shortcuts import render ,redirect
from django.http import HttpResponse
from . import forms
from datetime import date
import calendar
from .models import Family
from django.contrib.auth.decorators import login_required


# Create your views here.


def home_page(request):
    tmp = Family(12 ,"dsfadf", "fdjksf" , "dfjksf" , {"dfs":23})
    # tmp.family_id = 12
    # tmp.family_head
    tmp.save()
    return HttpResponse("asdfasdf")

def form(request):
    if request.method == "POST":
        print("submit" , request.POST)
        formset = forms.FamilyForm(request.POST, request.FILES)
        # print("form set", formset)
        formset.save()
        return redirect('/hajri/form')
    myform = forms.FamilyForm
    return render(request , 'form.html' , { "myform" : myform })

@login_required
def form1(request):
    if request.method == "POST":
        print("submit" , request.POST)
        formset = forms.form_sabha_attendance_entry(request.POST, request.FILES)
        # print("form set", formset)
        formset.save()
        return redirect('/hajri/form1')
    myform = forms.form_sabha_attendance_entry()
    date_of_sabha = date.today().strftime("%m/%d/%Y ")
    week_day_of_sabha = calendar.day_name[date.today().weekday()]
    today_date = date_of_sabha + " | " + week_day_of_sabha
    return render(request , 'form_hajri.html' , { 
        "myform" : myform , 
        "today_date" : today_date })
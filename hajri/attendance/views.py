from django.shortcuts import render ,redirect
from django.http import HttpResponse
from . import forms
from datetime import date
import calendar
# Create your views here.


def home_page(request):
    return HttpResponse("asdfasdf")

def form(request):
    if request.method == "POST":
        print("submit" , request.POST)
        formset = forms.PersonForm(request.POST, request.FILES)
        # print("form set", formset)
        formset.save()
        return redirect('/hajri/form')
    myform = forms.PersonForm
    return render(request , 'form.html' , { "myform" : myform })


def form1(request):
    if request.method == "POST":
        print("submit" , request.POST)
        formset = forms.date_personForm(request.POST, request.FILES)
        # print("form set", formset)
        formset.save()
        return redirect('/hajri/form1')
    myform = forms.date_personForm
    date_of_sabha = date.today().strftime("%m/%d/%Y ")
    week_day_of_sabha = calendar.day_name[date.today().weekday()]
    today_date = date_of_sabha + " | " + week_day_of_sabha
    return render(request , 'form_hajri.html' , { 
        "myform" : myform , 
        "today_date" : today_date })
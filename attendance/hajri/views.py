from django.shortcuts import render ,redirect
from django.http import HttpResponse
from . import forms
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
    return render(request , 'form.html' , { "myform" : myform })
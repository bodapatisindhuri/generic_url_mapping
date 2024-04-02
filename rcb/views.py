from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sindhu(request):
    return render(request,'virat.html')

def guru(request):
    return HttpResponse('Guru is my dad name')
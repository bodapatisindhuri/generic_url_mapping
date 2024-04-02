from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def sharma(request):
    return render(request,'sharma.html')

def bharathi(request):
    return HttpResponse('Bharath is MOM2')

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def Praba(request):
   
   return render(request, 'praba/intex.html')
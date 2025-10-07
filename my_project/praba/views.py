from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def Praba(request):
   return HttpResponse.render(request, 'praba/intext.html')
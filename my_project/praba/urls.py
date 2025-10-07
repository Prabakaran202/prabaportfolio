from django.urls import path
from . import views

urlpatterns = [
    path('praba/',views.Praba,name='Praba'),
]

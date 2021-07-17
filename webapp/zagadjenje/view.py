from django import template
from django.http import HttpResponse
from django.template import Template
from django.shortcuts import render
from requests import api
import obradaWeatherApija as wapi
from Proba import PredvidjanjeZagadjenja

k4 = PredvidjanjeZagadjenja()
k1 = PredvidjanjeZagadjenja()
lista_vrednosti_zagadjenja=k4.predvidjanje_zagadjenja_CETIRI_dana()
lista_zagadjenja_danas = k1.predvidjanje_zagadjenja_danas()
podaci_o_vremenu = wapi.obradaApi()

def home(request):
    return render(request, 'index.html', {
        'temperature': podaci_o_vremenu[2][0],
        'weather_descriptions': podaci_o_vremenu[2][4],
        'padavine': podaci_o_vremenu[2][1],
        'vetar_brz': podaci_o_vremenu[2][2],
        'vetar_dir': podaci_o_vremenu[2][3],
        'sutramin': podaci_o_vremenu[1][1],
        'sutramax': podaci_o_vremenu[0][1],
        'drugimin': podaci_o_vremenu[1][2],
        'drugimax': podaci_o_vremenu[0][2],
        'trecimin': podaci_o_vremenu[1][3],
        'trecimax': podaci_o_vremenu[0][3],
        'cetvrtimin': podaci_o_vremenu[1][4],
        'cetvrtimax': podaci_o_vremenu[0][4],
        'danasso2':round(lista_zagadjenja_danas[0]),
        'danaspm10':round(lista_zagadjenja_danas[1]),
        'danaspm25':round(lista_zagadjenja_danas[2]),
        'danasno2':round(lista_zagadjenja_danas[3]),
        'danaso3':round(lista_zagadjenja_danas[4]),
        'so21': lista_vrednosti_zagadjenja[0][0],
        'pm101': lista_vrednosti_zagadjenja[0][1],
        'pm251': lista_vrednosti_zagadjenja[0][2],
        'no21': lista_vrednosti_zagadjenja[0][3],
        'o31': lista_vrednosti_zagadjenja[0][4],
        'so22': lista_vrednosti_zagadjenja[1][0],
        'pm102': lista_vrednosti_zagadjenja[1][1],
        'pm252': lista_vrednosti_zagadjenja[1][2],
        'no22': lista_vrednosti_zagadjenja[1][3],
        'o32': lista_vrednosti_zagadjenja[1][4],
        'so23': lista_vrednosti_zagadjenja[2][0],
        'pm103': lista_vrednosti_zagadjenja[2][1],
        'pm253': lista_vrednosti_zagadjenja[2][2],
        'no23': lista_vrednosti_zagadjenja[2][3],
        'o33': lista_vrednosti_zagadjenja[2][4],
        'so24': lista_vrednosti_zagadjenja[3][0],
        'pm104': lista_vrednosti_zagadjenja[3][1],
        'pm254': lista_vrednosti_zagadjenja[3][2],
        'no24': lista_vrednosti_zagadjenja[3][3],
        'o34': lista_vrednosti_zagadjenja[3][4],

    })
def vesti(request):
    templejt = render(request,'news.html')
    return templejt

def kontakt(request):
    templejt = render(request,'contact.html') 
    return templejt

def fotke(request):
    templejt = render(request,'photos.html')
    return templejt

def kamere(request):
    templejt_heder = render(request,'cameras.html')
    return templejt_heder



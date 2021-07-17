import requests
import json
import datetime
import math

def obradaApi():
    response1 = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=Belgrade&exclude=hourly&units=metric&appid=20e9895767b61ac2c284df34d44612f4')

    narednidani = response1.json()
    trenutnisat=(int(str(datetime.datetime.now()).split(' ')[1].split(':')[0]))
    brojacsati = math.floor((trenutnisat-3)//3) if trenutnisat > 3 else 1
    maksimumi=[[],[],[],[],[]]
    minimumi=[[],[],[],[],[]]
    opisna_oblacnost = [[],[],[],[],[]]
    pritisak = [[],[],[],[],[]]
    vlaznost = [[],[],[],[],[]]
    vetar = [[],[],[],[],[]]
    oblacnost = [[],[],[],[],[]]

    trenutnovreme=[]
    for i in narednidani:
            if i =='list':
                for j in range(0,32+brojacsati):
                    if j == 0:
                        trenutnovreme.append(narednidani['list'][0]['main']['temp_max'])
                        trenutnovreme.append(narednidani['list'][0]['pop'])
                        trenutnovreme.append(narednidani['list'][0]['wind']['speed'])
                        trenutnovreme.append(narednidani['list'][0]['wind']['deg'])
                    if j < 8-brojacsati:
                        minimumi[0].append(narednidani['list'][j]['main']['temp_min'])
                        maksimumi[0].append(narednidani['list'][j]['main']['temp_max'])
                        opisna_oblacnost[0].append(narednidani['list'][j]['weather'][0]['main'])
                        pritisak[0].append(narednidani['list'][j]['main']['pressure'])
                        vlaznost[0].append(narednidani['list'][j]['main']['humidity'])
                        vetar[0].append(narednidani['list'][j]['wind']['speed'])
                        oblacnost[0].append(narednidani['list'][j]['clouds']['all'])
                        

                    elif j < 8+8-brojacsati:
                        minimumi[1].append(narednidani['list'][j]['main']['temp_min'])
                        maksimumi[1].append(narednidani['list'][j]['main']['temp_max'])
                        opisna_oblacnost[1].append(narednidani['list'][j]['weather'][0]['main'])
                        pritisak[1].append(narednidani['list'][j]['main']['pressure'])
                        vlaznost[1].append(narednidani['list'][j]['main']['humidity'])
                        vetar[1].append(narednidani['list'][j]['wind']['speed'])
                        oblacnost[1].append(narednidani['list'][j]['clouds']['all'])

                    elif j < 16+8-brojacsati:
                        minimumi[2].append(narednidani['list'][j]['main']['temp_min'])
                        maksimumi[2].append(narednidani['list'][j]['main']['temp_max'])
                        opisna_oblacnost[2].append(narednidani['list'][j]['weather'][0]['main'])
                        pritisak[2].append(narednidani['list'][j]['main']['pressure'])
                        vlaznost[2].append(narednidani['list'][j]['main']['humidity'])
                        vetar[2].append(narednidani['list'][j]['wind']['speed'])
                        oblacnost[2].append(narednidani['list'][j]['clouds']['all'])

                    elif j < 24+8-brojacsati:
                        minimumi[3].append(narednidani['list'][j]['main']['temp_min'])
                        maksimumi[3].append(narednidani['list'][j]['main']['temp_max'])
                        opisna_oblacnost[3].append(narednidani['list'][j]['weather'][0]['main'])
                        pritisak[3].append(narednidani['list'][j]['main']['pressure'])
                        vlaznost[3].append(narednidani['list'][j]['main']['humidity'])
                        vetar[3].append(narednidani['list'][j]['wind']['speed'])
                        oblacnost[3].append(narednidani['list'][j]['clouds']['all'])

                    elif j < 32+8-brojacsati:
                        minimumi[4].append(narednidani['list'][j]['main']['temp_min'])
                        maksimumi[4].append(narednidani['list'][j]['main']['temp_max'])
                        opisna_oblacnost[4].append(narednidani['list'][j]['weather'][0]['main'])
                        pritisak[4].append(narednidani['list'][j]['main']['pressure'])
                        vlaznost[4].append(narednidani['list'][j]['main']['humidity'])
                        vetar[4].append(narednidani['list'][j]['wind']['speed'])
                        oblacnost[4].append(narednidani['list'][j]['clouds']['all'])

    return [[round(max(maksimumi[0])),round(max(maksimumi[1])),round(max(maksimumi[2])),round(max(maksimumi[3])),round(max(maksimumi[4]))],
    [round(min(minimumi[0])), round(min(minimumi[1])), round(min(minimumi[2])), round(min(minimumi[3])), round(min(minimumi[4]))],[round(trenutnovreme[0]),(trenutnovreme[1]),(trenutnovreme[2]),(trenutnovreme[3]),opisna_oblacnost[0][0]]]

obradaApi()
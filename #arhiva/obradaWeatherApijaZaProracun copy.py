import requests
import json
import datetime
import math

#print (round(datetime.datetime.utcnow().timestamp()))


def zagadjenjejuce():
    jucerasnjezagadjenje = requests.get(f'http://api.openweathermap.org/data/2.5/air_pollution?lat=20.46&lon=44.8&start={(round(datetime.datetime.utcnow().timestamp()))-120000}&end={(round(datetime.datetime.utcnow().timestamp()))-120000}&appid=20e9895767b61ac2c284df34d44612f4')
    jucerasnjezagadjenje = jucerasnjezagadjenje.json()
    zagadjenjejuce = []
    for k in jucerasnjezagadjenje:
            if k =='list':
                zagadjenjejuce.append(jucerasnjezagadjenje['list'][0]['main']['aqi'])
                zagadjenjejuce.append(jucerasnjezagadjenje['list'][0]['components']['so2'])
                zagadjenjejuce.append(jucerasnjezagadjenje['list'][0]['components']['pm2_5'])
                zagadjenjejuce.append(jucerasnjezagadjenje['list'][0]['components']['pm10'])
    return zagadjenjejuce

def zagadjenjedanas():
    trenutnozagadjenje = requests.get('https://api.waqi.info/feed/belgrade/?token=2f7dbc852169c85cc4b283bc0de1f4eaad7c2938')
    trenutnozagadjenje = trenutnozagadjenje.json()
    podaciOvazduhu = []
    danas = trenutnozagadjenje['data']['time']['s']
    print(danas)
    for k in trenutnozagadjenje:
                podaciOvazduhu.append(trenutnozagadjenje['data']['iaqi']['so2']['v'])
                podaciOvazduhu.append(trenutnozagadjenje['data']['iaqi']['pm10']['v'])
                podaciOvazduhu.append(trenutnozagadjenje['data']['iaqi']['pm25']['v'])
                podaciOvazduhu.append(trenutnozagadjenje['data']['iaqi']['no2']['v'])
                podaciOvazduhu.append(trenutnozagadjenje['data']['iaqi']['o3']['v'])
    return podaciOvazduhu

def obradaApiZaProracun(dan):
    response1 = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=Belgrade&exclude=hourly&units=metric&appid=20e9895767b61ac2c284df34d44612f4')
    narednidani = response1.json()
    trenutnisat=(int(str(datetime.datetime.now()).split(' ')[1].split(':')[0]))
    #trenutnisat = 4
    brojacsati = math.floor((trenutnisat-3)//3) if trenutnisat >= 3 else 0
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
                for j in range(0,40+brojacsati):
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

    #print(maksimumi,minimumi,pritisak,vlaznost,vetar,oblacnost)
    # return [[round(max(maksimumi[0])),round(max(maksimumi[1])),round(max(maksimumi[2])),round(max(maksimumi[3])),round(max(maksimumi[4]))],
    # [round(min(minimumi[0])), round(min(minimumi[1])), round(min(minimumi[2])), round(min(minimumi[3])), round(min(minimumi[4]))],[round(trenutnovreme[0]),(trenutnovreme[1]),(trenutnovreme[2]),(trenutnovreme[3]),opisna_oblacnost[0][0]]]

    return [[pritisak[dan][0],pritisak[dan][-4],pritisak[dan][-2],sum(pritisak[dan])/len(pritisak[dan]),
    max(maksimumi[dan]),min(minimumi[dan]),(maksimumi[dan][1]+minimumi[dan][1])/2,(maksimumi[dan][4]+minimumi[dan][4])/2,(maksimumi[dan][6]+minimumi[dan][6])/2,(max(maksimumi[dan])+min(minimumi[dan]))/2,
    vlaznost[dan][1],vlaznost[dan][4],vlaznost[dan][6],sum(vlaznost[dan])/8,
    vetar[dan][1],vetar[dan][4],vetar[dan][6],sum(vetar[dan])/8,
    oblacnost[dan][1],oblacnost[dan][4],oblacnost[dan][6],sum(oblacnost[dan])/8,
    ],]


# print(zagadjenjedanas())
# print(obradaApiZaProracun(1))
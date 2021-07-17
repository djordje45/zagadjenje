import Modeli

data = [[1001.4,1000.4,1000.5,1000.8,31.6,21.5,10.1,18.2,23.4,31.2,26.2,26.8,69,45,71,62,19.9,20.3,24.1,21.4,0.8,2.4,0.8,1.4,1,4,0,1.7,6]]

SO2,PM10,PM25 = Modeli.racunanje_vrednosti(data)

def racunanje_AQI(SO2,PM10,PM25):
    if PM10 <= 100:
        PM10subindex = PM10 
    elif PM10 > 100 and PM10 <= 250:
        PM10subindex = 100+(PM10-100)*100/150
    elif PM10 > 250 and PM10 <= 350:
        PM10subindex = 200+(PM10-250)
    elif PM10 > 250 and PM10 <= 430:
        PM10subindex = 300+(PM10-350)*(100/80)
    else:
        PM10subindex = 400+(PM10-430)*(100/80)

    if PM25 <= 30:
        PM25subindex = PM25*50/30
    elif PM25 > 30 and PM25 <= 60:
        PM25subindex = 50+(PM25-30)*50/30
    elif PM25 > 60 and PM25 <= 90:
        PM25subindex = 100+(PM25-60)*100/30
    elif PM25 > 90 and PM25 <= 120:
        PM25subindex = 200+(PM25-90)*(100/30)
    else:
        PM25subindex = 300+(PM25-120)*(100/130)


    if SO2 <= 40:
        SO2subindex = SO2*50/40
    else:
        SO2subindex = 50+(SO2-40)*50/40
    
    return max(SO2,PM10,PM25)

print (racunanje_AQI(SO2,PM10,PM25))

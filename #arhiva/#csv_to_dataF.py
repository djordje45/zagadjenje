
from datetime import date
import numpy as np
import pandas as pd


class CsvVremePlusZagadjenje:
    def iscitavanje_iz_csv_i_upis_u_novi(self, file,godina):
        self.csvfajl = pd.read_csv('pm10.csv',sep=',')
        self.csvfajl = self.csvfajl.sort_values(by=['Column1'])
        self.p = pd.read_csv(file,sep=',')
        self.brojevi=('1','2','3','4','5','6','7','8','9')
        mesec = 0.5
        self.prva_polovina_podataka=pd.DataFrame()
        self.druga_polovina_podataka=pd.DataFrame()
        for i in range(len(self.p)):
            #print(p.loc[i])
            if self.p['Column1'][i].startswith(self.brojevi):
                if int(self.p['Column1'][i])==1:
                    mesec+=0.5
                if mesec%1==0:
                    self.datum = date(godina,int(np.floor(mesec)),int(self.p['Column1'][i]))
                    self.p['Column1'][i]=datum
                    self.prva_polovina_podataka = self.prva_polovina_podataka.append(p.loc[[i]],ignore_index=True)
                # print(p.loc[[i]])   
                elif mesec%1==0.5:
                    datum = date(godina,int(np.floor(mesec)),int(self.p['Column1'][i]))
                    self.p['Column1'][i]=datum
                    self.druga_polovina_podataka = self.druga_polovina_podataka.append(self.p.loc[[i]],ignore_index=True)
            else:
                self.p.drop(self.p.index[[i]],axis=0)

        
        self.podaci_za_celu_godinu = self.prva_polovina_podataka.merge(self.druga_polovina_podataka, how='inner', on='Column1')

        self.podaci_za_celu_godinu.replace(',','', inplace=True)
        return self.podaci_za_celu_godinu



    pod17 = iscitavanje_iz_csv_i_upis_u_novi(f'semicolon2017.csv',2017)
    pod18 = iscitavanje_iz_csv_i_upis_u_novi(f'semicolon2018.csv',2018)
    pod19 = iscitavanje_iz_csv_i_upis_u_novi(f'semicolon2019.csv',2019)


    svezajedno = pd.concat([pod17,pod18,pod19])

    pm10 = pd.read_csv('pm10.csv',sep=',')
    pm10 = pm10.sort_values(by=['Column1'])
    pm10.Column1 = pd.to_datetime(pm10.Column1)

    svezajedno.Column1 = pd.to_datetime(svezajedno.Column1)

    svezajedno = svezajedno.merge(pm10, how='inner', on='Column1')

    svezajedno = svezajedno.rename(columns={"Column1": "Date", "Column6_y":"wind1","Column8_y":"wind2",
    "Column10_y":"wind3", 'Column2_x':'Pritisak07', 'Column3_x':'Pritisak14', 'Column4_x':'Pritisak21', 'Column5_x':'PritisakSR', 'Column6_x':'MaxTemp',
    'Column7_x':'MinTemp', 'Column8_x':'AMP_Temp', 'Column10_x':'Temp07', 'Column11_x':'Temp14', 'Column12_x':'Temp21', 'Column13_x':'TempSR', 'Column14_x':'Vlaz07'
    , 'Column15_x':'Vlaz14', 'Column16_x':'Vlaz21', 'Column17_x':'VlazSR', 'Column2_y':'Napon07', 'Column3_y':'Napon14', 'Column4_y':'Napon21'
    , 'Column5_y':'NaponSR', 'Column7_y':'VetarBrzina07', 'Column9_y':'VetarBrzina14', 'Column11_y':'VetarBrzina21', 'Column12_y':'VetarBrzinaSR',
    'Column14_y':'Oblacnost07','Column15_y':'Oblacnost14','Column16_y':'Oblacnost21','Column17_y':'OblacnostSR'})

    nan_value = float("NaN")
    svezajedno.replace('.',nan_value, inplace=True)
    svezajedno.replace('-',nan_value, inplace=True)
    svezajedno.dropna(axis=1,thresh=720, inplace=True)
    svezajedno['prethodni_dan']=svezajedno['ValuePM10'].shift(periods=1)
    svezajedno['Value']=svezajedno['ValuePM10']
    svezajedno = svezajedno.drop(['ValuePM10'],axis=1)
    svezajedno = svezajedno.drop(index=0,axis=1)
    svezajedno.dropna(axis=0, inplace=True)
    svezajedno.to_csv('VremenskiPodaciZa3godine111.csv')


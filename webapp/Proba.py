#import ucitavanjemodela
import ucitavanjeXGB as ucitavanjemodela
import obradaWeatherApijaZaProracun as wapip

import numpy as np
from sklearn import preprocessing

minmax = preprocessing.MinMaxScaler()

class PredvidjanjeZagadjenja:
        def predvidjanje_zagadjenja_danas(self): #Koliko Dana Unapred
                self.datajuceo3, self.datajucepm10, self.datajucepm25, self.datajuceno2, self.datajuceso2 = wapip.zagadjenjedanas()[0],wapip.zagadjenjedanas()[1],wapip.zagadjenjedanas()[2],wapip.zagadjenjedanas()[3],wapip.zagadjenjedanas()[4]
                return self.datajuceso2, self.datajucepm10, self.datajucepm25, self.datajuceno2, self.datajuceo3

        def predvidjanje_zagadjenja_sutra(self):
                self.datajuceso2, self.datajucepm10, self.datajucepm25, self.datajuceno2, self.datajuceo3 = wapip.zagadjenjedanas()[0],wapip.zagadjenjedanas()[1],wapip.zagadjenjedanas()[2],wapip.zagadjenjedanas()[3],wapip.zagadjenjedanas()[4]
                self.datavreme10 = wapip.obradaApiZaProracun(1)
                self.datavreme25 = wapip.obradaApiZaProracun(1)
                self.datavremeso2 = wapip.obradaApiZaProracun(1)
                self.datavremeno2 = wapip.obradaApiZaProracun(1)
                self.datavremeo3 = wapip.obradaApiZaProracun(1)
                self.datavreme10[0].append(self.datajucepm10)
                self.datavreme25[0].append(self.datajucepm25)
                self.datavremeso2[0].append(self.datajuceso2)
                self.datavremeno2[0].append(self.datajuceno2)
                self.datavremeo3[0].append(self.datajuceo3)
                return (ucitavanjemodela.prognoziranje(np.array(self.datavremeso2), np.array(self.datavreme10), np.array(self.datavreme25),np.array(self.datavremeno2),np.array(self.datavremeo3)))

        def predvidjanje_zagadjenja_dva_dana(self):
                [self.sutraso2, self.sutrapm10, self.sutrapm25, self.sutrano2, self.sutrao3] = self.predvidjanje_zagadjenja_sutra()
                self.datavreme10 = wapip.obradaApiZaProracun(2)
                self.datavreme25 = wapip.obradaApiZaProracun(2)
                self.datavremeso2 = wapip.obradaApiZaProracun(2)
                self.datavremeno2 = wapip.obradaApiZaProracun(2)
                self.datavremeo3 = wapip.obradaApiZaProracun(2)
                self.datavreme10[0].append(self.sutrapm10)
                self.datavreme25[0].append(self.sutrapm25)
                self.datavremeso2[0].append(self.sutraso2)
                self.datavremeno2[0].append(self.sutrano2)
                self.datavremeo3[0].append(self.sutrao3)
                #self.datajuceso2, self.datajucepm25,self.datajucepm10 = (Modeli.racunanje_vrednosti(self.datavreme10, self.datavreme25, self.datavremeso2))

                return (ucitavanjemodela.prognoziranje(np.array(self.datavremeso2), np.array(self.datavreme10), np.array(self.datavreme25),np.array(self.datavremeno2),np.array(self.datavremeo3))),[self.sutraso2, self.sutrapm10, self.sutrapm25,self.sutrano2,self.sutrao3]

        def predvidjanje_zagadjenja_TRI_dana(self):
                [self.sutraso2, self.sutrapm10, self.sutrapm25, self.sutrano2, self.sutrao3], self.danpre = self.predvidjanje_zagadjenja_dva_dana()
                self.datavreme10 = wapip.obradaApiZaProracun(3)
                self.datavreme25 = wapip.obradaApiZaProracun(3)
                self.datavremeso2 = wapip.obradaApiZaProracun(3)
                self.datavremeno2 = wapip.obradaApiZaProracun(3)
                self.datavremeo3 = wapip.obradaApiZaProracun(3)
                self.datavreme10[0].append(self.sutrapm10)
                self.datavreme25[0].append(self.sutrapm25)
                self.datavremeso2[0].append(self.sutraso2)
                self.datavremeno2[0].append(self.sutrano2)
                self.datavremeo3[0].append(self.sutrao3)
                #self.datajuceso2, self.datajucepm25,self.datajucepm10 = (Modeli.racunanje_vrednosti(self.datavreme10, self.datavreme25, self.datavremeso2))
                return (ucitavanjemodela.prognoziranje(np.array(self.datavremeso2), np.array(self.datavreme10), np.array(self.datavreme25),np.array(self.datavremeno2),np.array(self.datavremeo3))),[self.sutraso2, self.sutrapm10, self.sutrapm25,self.sutrano2,self.sutrao3],self.danpre

        #print(predvidjanje_zagadjenja_TRI_dana())


        def predvidjanje_zagadjenja_CETIRI_dana(self):
                [self.sutraso2, self.sutrapm10, self.sutrapm25, self.sutrano2, self.sutrao3],self.danpre,self.dvadanapre = self.predvidjanje_zagadjenja_TRI_dana()
                self.datavreme10 = wapip.obradaApiZaProracun(4)
                self.datavreme25 = wapip.obradaApiZaProracun(4)
                self.datavremeso2 = wapip.obradaApiZaProracun(4)
                self.datavremeno2 = wapip.obradaApiZaProracun(4)
                self.datavremeo3 = wapip.obradaApiZaProracun(4)
                self.datavreme10[0].append(self.sutrapm10)
                self.datavreme25[0].append(self.sutrapm25)
                self.datavremeso2[0].append(self.sutraso2)
                self.datavremeno2[0].append(self.sutrano2)
                self.datavremeo3[0].append(self.sutrao3)
                #self.datajuceso2, self.datajucepm25,self.datajucepm10 = (Modeli.racunanje_vrednosti(self.datavreme10, self.datavreme25, self.datavremeso2))
                return self.dvadanapre, self.danpre,[self.sutraso2, self.sutrapm10, self.sutrapm25,self.sutrano2,self.sutrao3],\
                        (ucitavanjemodela.prognoziranje(np.array(self.datavremeso2), np.array(self.datavreme10), np.array(self.datavreme25),np.array(self.datavremeno2),np.array(self.datavremeo3)))
                



# k = PredvidjanjeZagadjenja()
# print(k.predvidjanje_zagadjenja_CETIRI_dana())
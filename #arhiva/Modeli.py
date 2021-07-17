import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from sklearn import preprocessing

class NeuralnaMreza:
    def __init__(self, fajltrening, fajltest):
        self.dftrain = pd.read_csv(fajltrening)
        self.dfeval = pd.read_csv(fajltest)
        self.dfeval.replace(',','',inplace=True)
        self.dftrain.replace(',','',inplace=True)
        self.y_train = self.dftrain.pop("Value")
        self.y_train = self.y_train.astype(int)
        self.y_eval =self.dfeval.pop('Value')
        self.y_eval = self.y_eval.astype(int)
        (self.x_train, self.y_train), (self.x_test, self.y_test) = (self.dftrain,self.y_train),(self.dfeval,self.y_eval)
        
    def napravi_model(self,izlaz):
        self.model = keras.Sequential([
        keras.layers.Flatten(input_shape=(self.x_train.shape[1],)),  # ulazni sloj (1)
        keras.layers.Dense(348, activation='relu'),  # skriveni sloj (2)
        keras.layers.Dense(izlaz, activation='softmax')]) # izlazni  sloj (3)
        self.model.compile(optimizer='adam',
                    loss='SparseCategoricalCrossentropy',
                    metrics=['TopKCategoricalAccuracy'])

        self.model.fit(self.x_train, self.y_train, epochs=65,verbose=0)  

        test_loss, test_acc = self.model.evaluate(self.x_test,  self.y_test, verbose=0) 
        self.predictions = self.model.predict(self.x_test,verbose=0)
        #prognoza = model.predict(podaci_za_predvidjanje,verbose=0)
        #return np.argmax(prognoza[0])
        print('Test accuracy:', test_acc)


    def sacuvaj_model(self,NAME):
        self.model.save(f'{NAME}model')

    def proveri_rez(self):
        k=0                                                   #Provera preciznosti modela
        for i in range(132):    
            print(np.argmax(self.predictions[i]),end=', ')
            #print(predictions[i])
            print(self.y_test[i])
            k+=abs(np.argmax(self.predictions[i])-self.y_test[i])
            #print(k)
        print(k/132)


PM10neur = NeuralnaMreza('cesticecsv/PM10train1.csv', 'cesticecsv/PM10test1.csv')
PM10neur.napravi_model(126)
PM10neur.proveri_rez()





#data = [[1001.4,1000.4,1000.5,1000.8,31.6,21.5,10.1,18.2,23.4,31.2,26.2,26.8,69,45,71,62,19.9,20.3,24.1,21.4,0.8,2.4,0.8,1.4,1,4,0,1.7,6]]

# def racunanje_vrednosti(dataSO2, dataPM10, dataPM25 ):
#     return(napravi_model('cesticecsv/SO2train.csv', 'cesticecsv/SO2Test.csv', 26,dataSO2 )),(napravi_model('cesticecsv/PM10train1.csv', 'cesticecsv/PM10test1.csv', 126,dataPM10 )),(napravi_model('cesticecsv/PM25train.csv', 'cesticecsv/PM25test.csv', 240 ,dataPM25))


#napravi_model('cesticecsv/SO2train.csv', 'cesticecsv/SO2Test.csv', 26,'SO2' )
#napravi_model('cesticecsv/PM10train1.csv', 'cesticecsv/PM10test1.csv', 126,'PM10')
#napravi_model('cesticecsv/PM25train.csv', 'cesticecsv/PM25test.csv', 240 ,'PM25')
# napravi_model('cesticecsv/NO2train.csv', 'cesticecsv/NO2test.csv', 55 ,'NO2')
#napravi_model('cesticecsv/O3train.csv', 'cesticecsv/O3test.csv', 80 ,'O3')

from sklearn import model_selection
from sklearn import neighbors
from sklearn import svm,preprocessing
import pandas as pd
import numpy as np


class Kneighbor:
    def __init__(self, testcsv,traincsv):    
        self.features_train = pd.read_csv(testcsv)
        self.features_test = pd.read_csv(traincsv)
        self.features_train.replace(',','.',inplace=True)
        self.features_test.replace(',','.',inplace=True)
        self.label_train = self.features_train.pop("Value")
        self.label_train = self.label_train.astype(int)
        self.label_test = self.features_test.pop('Value')
        self.label_test = self.label_test.astype(int)

        self.features_train = preprocessing.MinMaxScaler(feature_range=(0,1),clip=True,).fit_transform(self.features_train)
        self.features_test = preprocessing.MinMaxScaler(feature_range=(0,1),clip=True,).fit_transform(self.features_test)

        self.classifier = neighbors.KNeighborsClassifier()
        self.classifier.fit(self.features_train, self.label_train)
        self.classifier.score(self.features_test, self.label_test)

        print('Model score: ', self.classifier.score(self.features_test, self.label_test))
        #print('\n')

        k=0
        for i in range (130):
            data_point = self.features_test[i]
            data_point = np.array(data_point)
            data_point = data_point.reshape(1, -1)

            print('Predikcija-> ', round(self.classifier.predict(data_point)[0]), self.label_test[i]," <-Stvarna vrednost")
            k+=abs(self.classifier.predict(data_point)-self.label_test[i])
            #print(k)
        print('Prosecna greska:',k/130)

no2 = Kneighbor('cesticecsv/no2Test.csv','cesticecsv/no2Train.csv')

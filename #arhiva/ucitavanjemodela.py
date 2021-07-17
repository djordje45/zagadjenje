import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from sklearn import preprocessing


def prognoziranje(dataso2, datapm10,datapm25, datano2, datao3):
    reconstructed_model_so2 = keras.models.load_model("SO2model")
    reconstructed_model_pm10 = keras.models.load_model("PM10model")
    reconstructed_model_pm25 = keras.models.load_model("PM25model")
    reconstructed_model_no2 = keras.models.load_model("NO2model")
    reconstructed_model_o3 = keras.models.load_model("O3model")
    prognozaSo2 = reconstructed_model_so2.predict(dataso2,verbose=0)
    prognozapm10 = reconstructed_model_pm10.predict(datapm10,verbose=0)
    prognozapm25 = reconstructed_model_pm25.predict(datapm25,verbose=0)
    prognozano2 = reconstructed_model_no2.predict(datano2,verbose=0)
    prognozao3 = reconstructed_model_o3.predict(datao3,verbose=0)
    return np.argmax(prognozaSo2[0]),np.argmax(prognozapm10[0]),np.argmax(prognozapm25[0]),np.argmax(prognozano2[0]),np.argmax(prognozao3[0])


# data = np.array([[1001.4,1000.4,1000.5,1000.8,31.6,21.5,10.1,18.2,23.4,31.2,26.2,26.8,69,21.4,0.8,2.4,0.8,1.4,1,4,0,1.7,6]])


# reconstructed_model_so2 = keras.models.load_model("O3model")
# prognozaso2 = reconstructed_model_so2(data)

# print(np.argmax(prognozaso2[0]))

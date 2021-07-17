import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from sklearn import preprocessing
import xgboost as xgb
from sklearn.metrics import mean_squared_error


def prognoziranje(dataso2, datapm10,datapm25, datano2, datao3):
    reconstructed_model_so2 = xgb.XGBRegressor()
    reconstructed_model_pm10 = xgb.XGBRegressor()
    reconstructed_model_pm25 = xgb.XGBRegressor()
    reconstructed_model_no2 = xgb.XGBRegressor()
    reconstructed_model_o3 = xgb.XGBRegressor()
    reconstructed_model_so2.load_model("SO2modelXGBOOST")
    reconstructed_model_pm10.load_model("PM10modelXGBOOST")
    reconstructed_model_pm25.load_model("PM25modelXGBOOST")
    reconstructed_model_no2.load_model("NO2modelXGBOOST")
    reconstructed_model_o3.load_model("O3modelXGBOOST")
    return round(reconstructed_model_so2.predict(dataso2)[0]),round(reconstructed_model_pm10.predict(datapm10)[0]),round(reconstructed_model_pm25.predict(datapm25)[0]),round(reconstructed_model_no2.predict(datano2)[0]),round(reconstructed_model_o3.predict(datao3)[0])


# data = np.array([[1001.4,1000.4,1000.5,1000.8,31.6,21.5,10.1,18.2,23.4,31.2,26.2,26.8,69,21.4,0.8,2.4,0.8,1.4,1,4,0,1.7,6]])


# reconstructed_model_so2 = keras.models.load_model("O3model")
# prognozaso2 = reconstructed_model_so2(data)

# print(prognoziranje(data,data,data,data,data))
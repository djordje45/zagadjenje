import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from sklearn import preprocessing

dftrain = pd.read_csv('cesticecsv/PM10train1.csv')
dfeval = pd.read_csv('cesticecsv/PM10test1.csv')
dfeval.replace(',','',inplace=True)
dftrain.replace(',','',inplace=True)
y_train = dftrain.pop("Value")
y_train = y_train.astype(int)
y_eval = dfeval.pop('Value')
y_eval = y_eval.astype(int)
(x_train, y_train), (x_test, y_test) = (dftrain,y_train),(dfeval,y_eval)
 
print(x_train.shape)
print(y_train.shape)
 
print(x_test.shape)
print(y_test.shape)

minmax = preprocessing.MinMaxScaler()
x_train = minmax.fit_transform(x_train)
x_test = minmax.fit_transform(x_test)

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(1,29)),  # input layer (1)
    keras.layers.Dense(348, activation='relu'),  # hidden layer (2)
    keras.layers.Dense(126, activation='softmax') # output layer (3)
])

model.compile(optimizer='Adam',
              loss='SparseCategoricalCrossentropy',
              metrics=['TopKCategoricalAccuracy'])

model.fit(x_train, y_train, epochs=65)  # we pass the data, labels and epochs and watch the magic!

test_loss, test_acc = model.evaluate(x_test,  y_test, verbose=1) 

print('Test accuracy:', test_acc)

predictions = model.predict(x_test)
k=0
for i in range(132):    
    print(np.argmax(predictions[i]),end=', ')
    print(y_test[i])
    k+=abs(np.argmax(predictions[i])-y_test[i])
    print(k)
print(k/132)
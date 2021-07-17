
import xgboost as xgb
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt 
import pandas as pd


class XGBTreeRegression:
    def __init__(self,cesticetrain,cesticetest,param):
        self.dftrain = pd.read_csv(cesticetrain)
        self.dfeval = pd.read_csv(cesticetest)
        self.dfeval.replace(',','',inplace=True)
        self.dftrain.replace(',','',inplace=True)
        self.y_train = self.dftrain.pop("Value")
        self.y_train = self.y_train.astype(int)
        self.y_eval = self.dfeval.pop('Value')
        self.y_eval = self.y_eval.astype(int)
        self.xg_reg = xgb.XGBRegressor(**param)
        
    def napravi_model(self,imemodela):
        self.xg_reg.fit(self.dftrain, self.y_train, eval_metric='mae')
        self.score = self.xg_reg.score(self.dftrain, self.y_train)  
        print("Training score: ", self.score)
        self.ypred = self.xg_reg.predict(self.dfeval)
        mse = mean_squared_error(self.y_eval, self.ypred)
        print("MSE: %.2f" % mse)
        MSE: 3.35
        print("RMSE: %.2f" % (mse**(1/2.0)))
        RMSE: 1.83 
        self.x_ax = range(len(self.y_eval))
        plt.plot(self.x_ax, self.y_eval , label="original")
        plt.plot(self.x_ax, self.ypred, label="predicted")
        plt.title(imemodela)
        plt.legend()
        plt.show()
        return self.xg_reg, self.dfeval, self.y_eval
        
    def sacuvaj_model(self,NAME):
        self.xg_reg.save_model(NAME)


param = {'eta':0.1,'min_child_weight':1,'max_depht':12,'n_estimators':33,'gamma':1, 'reg_lambda':3}
c = XGBTreeRegression('cesticecsv/SO2train.csv', 'cesticecsv/SO2test.csv',param)
x, y, z = c.napravi_model('PM25modelXGBOOST')


# napravi_model('cesticecsv/PM10train1.csv', 'cesticecsv/PM10Test1.csv','PM10modelXGBOOST')
# napravi_model('cesticecsv/PM25train.csv', 'cesticecsv/PM25Test.csv' ,'PM25modelXGBOOST')
# napravi_model('cesticecsv/NO2train.csv', 'cesticecsv/NO2test.csv', 'NO2modelXGBOOST')
# x, y, z = napravi_model('cesticecsv/O3Train.csv','cesticecsv/O3Test.csv','O3modelXGBOOST')


k=0                                                   #Provera preciznosti modela
for i in range(132):    
            print(round(x.predict(y)[i]),end=', ')
            #print(predictions[i])
            print(z[i])
            k+=abs(round(x.predict(y)[i])-z[i])
            #print(k)
print(k/132)

# reconstructed_model_so2 = xgb.XGBRegressor({'nthread':4,'eta':0.1,'min_child_weight':2,'max_depht':32})
# reconstructed_model_so2.load_model("SO2modelXGBOOST")
# print(reconstructed_model_so2.predict('cesticecsv/PM25Test.csv'))
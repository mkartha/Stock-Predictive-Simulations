#Ridge Regression implementation
#Best utilized for linear/stable markets
#IMPORTANT: THIS IS SOLELY EDUCATIONAL AND EXPERIMENTAL, NOT FOR REAL MARKET USE
#Simulates Stock Data using time-series target vectors and feature matrices
#Completed on November 28 2025
#© MK 2025, All Rights Reserved



import yfinance as yf
import pandas as pd
import matplotlib.pyplot as mp
from datetime import date
import numpy as np
import random
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error


class RidgeReg:

    def __init__(self,ticker, st):
        raw=yf.download(ticker, start=st, end=date.today(), interval="1mo", progress=False)
        df=pd.DataFrame(raw)
        df_cleaned=df.dropna()
        self.stock_data=df_cleaned
        self.returns=None
        self.bootstrap_array=None
   
    def calculate_returns(self):
        opens=self.stock_data["Open"]
        opens=opens.squeeze()
        data_returns = []
        for i in range(len(opens) - 1):
            tStock = opens.iloc[i]
            nStock = opens.iloc[i+1]
            data_returns.append(np.log(nStock/tStock))
        self.returns=data_returns
        return self.returns


    #Initialize a feature 2D Array given a timeseries array
    def init_features(self, tsarr):
        if (len(tsarr)<=5):
            print("This is too small of an array")
            return
        mat=np.empty((len(tsarr)-5,4))
        for i in range(5,len(tsarr)):
            prev=tsarr[i-1]
            arr_elem=tsarr[i-5:i]
            mean=np.mean(arr_elem)
            std_dev=np.std(arr_elem)
            sum=np.sum(arr_elem)
            mat[i-5]=[prev,mean,std_dev,sum]
        return mat

    def init_target_vector(self,tsarr):
        if(len(tsarr)<=5):
            print("Too small of an array")
            return
        arr=[]
        for i in range(5,len(tsarr)):
            arr.append(tsarr[i])
        return arr
    
    def pred_nmonths_in_future(self, nmonths, matrix,tsarr, vector):
        y_pred=0.00
        X_train, X_test, Y_train, Y_test = train_test_split(matrix, vector, test_size=0.2, random_state=42)
        model=Ridge(alpha=1.0)
        model.fit(X_train, Y_train)
        y_pred=model.predict(X_test)
        mse=mean_squared_error(Y_test, y_pred)
        rmse=np.sqrt(mse)

        #To understand the error metric in the model for determining the accuracy of the mode
        print(rmse)
        
        arr=list(tsarr[-5:])
        pred_arr=[]
        for _ in range(nmonths):
            prev=arr[-1]
            mean=np.mean(arr)
            std=np.std(arr)
            s=np.sum(arr)
            feat=[[prev,mean,std,s]]
            future_pred=model.predict(feat)[0]
            r_e=arr.pop(0)
            arr.append(future_pred)
            pred_arr.append(future_pred)
        
        return arr[-1], pred_arr
    
    def visualize_data(self, nmonths, matrix, tsarr, vector):
        last_pred, yret=self.pred_nmonths_in_future(nmonths, matrix, tsarr, vector)
        P0 = self.stock_data["Open"].iloc[-1]
        y = [P0]
        for i in yret:
            y.append(y[-1]*np.exp(i))
        x=np.arange(0,nmonths+1)
        mp.scatter(x,y,color='black', marker='o')
        mp.plot(x,y,color='purple',linestyle='-')
        mp.xlabel("Month")
        mp.ylabel("Simulated Stock price")
        mp.show()

    


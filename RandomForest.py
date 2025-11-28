import yfinance as yf
import pandas as pd
import matplotlib.pyplot as mp
from datetime import date
import numpy as np
import random

class RandomForest:

    def __init__(self,ticker, st):
        raw=yf.download(ticker, start=st, end=date.today(), interval="1mo", progress=False)
        df=pd.DataFrame(raw)
        df_cleaned=df.dropna()
        self.stock_data=df_cleaned
        self.returns=None
        self.bootstrap_array=None
    def calculate_returns(self):
        data_returns=[]
        for i in range(len(self.stock_data["Open"]) - 1):
            tStock=self.stock_data["Open"].iloc[i]
            nStock=self.stock_data["Open"].iloc[i+1]
            data_returns.append(np.log(nStock/tStock))
        self.returns=data_returns
        return self.returns

    #Initialize Bootstrapped array from returns
    def init_bsarr(self, size=60):
        if self.returns is None:
            self.calculate_returns()
        bsarr=random.sample(self.returns,60)

    #Initialize a featur


import yfinance as yf
import pandas as pd
import matplotlib as mp
from datetime import date
import numpy as np

class MonteCarlo:

  #Constructor
  def __init__(self,ticker, st):
    self.stock_data=yf.download(ticker, start=st, end=date.today(), interval="1mo", progress=False)
    self.returns=None

  def calculate_returns(self):
    data_returns=[]
    for i in range(self.stock_data):
      if(i<len(self.stock_data["Open"])-1):
        tStock=self.stock_data["Open"].iloc[i]
        nStock=self.stock_data["Open"].iloc[i+1]
        data_returns.append(np.log(nStock/tStock))
        i+=1
        self.returns=data_returns;
    return self.returns
  
      
    

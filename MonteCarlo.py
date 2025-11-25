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

  #Calculate stock volatility(Standard Deviation)
  def calc_volatility(self):
    self.volatility=np.std(self.returns)
    return self.volatility

  #Calculate drift(Mean)
  def calc_drift(self):
    self.drift=np.mean(self.returns)
    return self.drift

  #Monte carlo simulation using GBM
  def simulate_month_ahead(self, months_ahead, n_sims):
    T=months_ahead/12.0
    last_m=self.returns[-1]
    m_carlo=[]
    for i in range(n_sims):
      Z=np.random.normal()
      future_log_return = ((self.drift - 0.5 * self.volatility**2) * T + self.volatility * np.sqrt(T) * Z)
      m_carlo.append(tr)
    expected_return=np.mean(m_carlo)
    closing_price=self.stock_data["Adj Close"].iloc[-1]
    p_value=closing_price+(closing_price*np.exp(expected_return))
    return p_value
      
  
    
  
      
    

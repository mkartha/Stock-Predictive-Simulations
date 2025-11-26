#Monte Carlo implementation for Stock Predictive Simulations
#Best Utilized for Bull Markets
#Simulates Stock Data with Random Shocks and Inflation Control
#Using Geometric Brownian Motion
#Completed on November 25 2025
#© MK 2025, All Rights Reserved


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as mp
from datetime import date
import numpy as np

class MonteCarlo:

  #Constructor
  def __init__(self,ticker, st):
    raw=yf.download(ticker, start=st, end=date.today(), interval="1mo", progress=False)
    df=pd.DataFrame(raw)
    df_cleaned=df.dropna()
    self.stock_data=df_cleaned
    self.returns=None
    self.volatility=None
    self.drift=None

  def calculate_returns(self):
    data_returns=[]
    for i in range(len(self.stock_data["Open"]) - 1):
      tStock=self.stock_data["Open"].iloc[i]
      nStock=self.stock_data["Open"].iloc[i+1]
      data_returns.append(np.log(nStock/tStock))
    self.returns=data_returns
    return self.returns

  #Calculate stock volatility(Standard Deviation)
  def calc_volatility(self):
    if self.returns is None:
      self.calculate_returns()
    self.volatility=np.std(self.returns)
    return self.volatility

  #Calculate drift(Mean)
  def calc_drift(self):
    if self.returns is None:
      self.calculate_returns()
    self.drift=np.mean(self.returns)
    return self.drift

  #Monte carlo simulation using GBM
  def simulate_month_ahead(self, months_ahead, n_sims):
    if self.drift is None:
      self.calc_drift()
    
    if self.volatility is None:
      self.calc_volatility()
    
    T=months_ahead
    m_carlo=[]
    closing_price=self.stock_data["Close"].iloc[-1]
    for i in range(n_sims):
      Z=np.random.normal()
      tr=((self.drift - 0.5 * self.volatility**2) * T + self.volatility * np.sqrt(T) * Z)
      m_carlo.append(np.exp(tr))
    e_p=closing_price*np.mean(m_carlo)
    return e_p
  
  #Visualize n_month random simulations
  def visualize_randoms(self, n_months):
    x=np.arange(1,n_months+1)
    y=[]
    for i in range(1,n_months+1):
      rand=self.simulate_month_ahead(i,1000)
      y.append(rand)
    mp.scatter(x,y,color='black', marker='o')
    mp.plot(x,y,color='purple',linestyle='-')
    mp.xlabel("Month")
    mp.ylabel("Simulated Stock price")
    mp.show()


      
  
    
  
      
    

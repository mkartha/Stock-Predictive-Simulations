import yfinance as yf
import pandas as pd
import matplotlib as mp
from datetime import date

class MonteCarlo:

  #Constructor
  def __init__(ticker, st):
    self.stock_data=yf.download(ticker, start=st, end=date.today(), interval="1mo", progress=False)
    self.returns=[]
    for 
    

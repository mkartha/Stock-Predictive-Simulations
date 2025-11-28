#Provides framework for implementing the MonteCarlo, Ridge Regression, and RandomForest libraries
import MonteCarlo
import RandomForest
import RidgeReg
import TestMarket


print("Hello! Welcome to Stock Predictive Simulations. Remember, this model is solely for experimental/educational purposes and should not be used to make real investment decisions.")
try:
    tester=None
    ticker=input("What stock do you want to analyze, enter the ticker symbol: ")
    months=int(input("Enter the number of months you want to predict for: "))
    date=input("Enter the start date as YYYY-MM-DD: ")
    ind=TestMarket.askQ()
    if(ind=="Bull"):
        tester=MonteCarlo.MonteCarlo(ticker, date)
    if(ind=="Neutral"):
        tester=RidgeReg.RidgeReg(ticker, date)
    if(ind=="Bear"):
        tester=RandomForest.RandomForest(ticker,date)
       
        '''
        Implement the individual methods for tester here
        '''
except Exception as e:
    print("Invalid entry. Please try again")

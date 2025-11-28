class TestMarket:

  @staticmethod
  def askQ():
    tScore=0
    print("Answer these questions as honestly as possible to capture the most accurate representations. 1 being each situation is not very prevalent(least importance), and 5 being the situation being very prevalent(most importance)")
    sTech=int(input("If the corporation you are trying to analyze is tech, rate the current growth of the tech market"))
    sEco=int(input("How stressed would you say the current U.S. Economy is due to various factors (e.g. Recession, Inflation)"))
    sMT=int(input("On a scale of 1-5(1 being not much increasing trend, and 5 being clear increasing), how increasing would you say the current market is?"))
    sDR=int(input("Rate the predictability of the market (1 = very unpredictable, 5 = very predictable)"))
    tScore=(0.4*(5-sEco))+(0.25*(sTech))+(0.25*(sMT))+(0.1*(sDR))
    if tScore>2.9:
      return "Bull"
    if tScore<=2.9 and tScore>=2.3:
      return "Neutral"
    if tScore<2.3:
      return "Bear"

    

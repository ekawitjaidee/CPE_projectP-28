"# Development-of-Technical-Signal-Analysis-System-for-Stock-Trading-using-Machine-Learning-Algorithm" 

1.Create GroundTruth
  1.1 Save_to_csv.ipynb : Use to load stock from yahoo finance api and we save to csv for label 3 class (1.Buy 2.Sell 3.Wait or Hold) 
  		     save to GT directory

2.Create Indicator
  2.1 DMI parameter.ipynb : Use to find a parameter most pofitable of Dmi Indicator
  2.2 MACD parameter.ipynb : Use to find a parameter most pofitable of MACD Indicator using Genatic Algorithm(Use GA.py) 
  2.3 Prepocess.ipynb : Use to add indicator to stock data
  #All file use stock data from GT directory
3.Training Model
  3.1 Model_LSTM.ipynb : Use to train a model for prediction
  #Use Dataset directory to open stock data
4.Simulation
  4.1 buyhold.ipynb : use to simulate buy and hold trades
  4.2 simulation.ipynb : use to simulate our model trades (#use Model_LSTM.h5)
5.Dataset and etc
  -Files required for the program
Python Library
-Pandas
-numpy
-matplotlib
-pandas_datareader(Get Stock data from yahoofinance api)
-datetime
-finplot(version 1.2.1)
-ta(version 0.7)
-glob
-keras
-sklearn
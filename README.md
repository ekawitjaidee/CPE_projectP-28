"# Development-of-Technical-Signal-Analysis-System-for-Stock-Trading-using-Machine-Learning-Algorithm" 

1.Create GroundTruth<br />
  1.1 Save_to_csv.ipynb : Use to load stock from yahoo finance api and we save to csv for label 2 class (1.Uptrend 2.Downtrend) 
  		     save to GT directory<br />

2.Create Indicator<br />
  2.1 DMI parameter.ipynb : Use to find a parameter most pofitable of Dmi Indicator<br />
  2.2 MACD parameter.ipynb : Use to find a parameter most pofitable of MACD Indicator using Genatic Algorithm(Use GA.py)<br /> 
  2.3 Prepocess.ipynb : Use to add indicator to stock data<br />
  #All file use stock data from GT directory<br />
  <br />
3.Training Model<br />
  3.1 Model_LSTM.ipynb : Use to train a model for prediction<br />
  #Use Dataset directory to open stock data<br />
  <br />
4.Simulation<br />
  4.1 buyhold.ipynb : use to simulate buy and hold trades<br />
  4.2 simulation.ipynb : use to simulate our model trades (#use Model_LSTM.h5)<br />
<br />
5.Dataset and etc<br />
  -Files required for the program<br />
  <br />
Python Library(require)<br />
-Pandas<br />
-numpy<br />
-matplotlib<br />
-pandas_datareader(Get Stock data from yahoofinance api)<br />
-datetime<br />
-finplot(version 1.2.1)<br />
-ta(version 0.7)<br />
-glob<br />
-keras<br />
-sklearn<br />

import glob
import pandas as pd
import numpy as np
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime
from keras.models import load_model 

from Indicator import Indicator
from GA import GA

def norm(df,col_name):# this will get columnname + _n
    #Normalize data each colunm in to range -1 to 1
    df[col_name+'_n'] = 2*(df[col_name]-df[col_name].min())/(df[col_name].max()-df[col_name].min())-1    
    return df

def add_shift_day(data,day):
    r_list = []
    for i in range(day,len(data)):#Number mean day to shift
        r_list.append(data[i-day : i])
    return np.array(r_list)

def PredictThreshold(y):
  pred = []
  last = np.argmax(y[0],-1)
  for c in y:

      if c[0]>0.8:
          pred.append(0)
          last = 0
      elif c[1]>0.8:
          pred.append(1)
          last = 1
      else:
          pred.append(last)
  return pred


model = load_model('model_LSTM.h5')
name = ''
stocklist = []
while name!='!':
    name = input('Stock Name (to exit typing !): ')
    if name =='!':
        break
    print('Start Date')
    sy,sm,sd = map(int,input('Y,M,D :').split(','))
    print('End Date')
    ey,em,ed = map(int,input('Y,M,D :').split(','))
    stocklist.append([name,[sy,sm,sd],[ey,em,ed]])
print(stocklist)
for stock in stocklist:
    try:
        st1,st2,st3 = stock[1][0],stock[1][1],stock[1][2]
        ed1,ed2,ed3 = stock[2][0],stock[2][1],stock[2][2]
        start = datetime.datetime(st1-3,st2,st3)
        end = datetime.datetime(ed1,ed2,ed3)
        df = web.DataReader(stock[0],'yahoo',start,end)
        df = Indicator().MACD(df,49,57,53)
        df = Indicator().DMI(df,48)
        df = Indicator().RSI(df)
        df = Indicator().WILLIANSR(df)
        df = Indicator().STOCHASTIC(df)
        df['STOCH'] = df['%K']-df['%D']
        df['MACD-SL'] = df['MACD'] - df['SIGNAL LINE']
        df['DMI'] = df['plusDI'] - df['minusDI']
        
        #MACD
        df = norm(df,'MACD')
        df = norm(df,'SIGNAL LINE')
        df = norm(df,'MACD-SL')
        #DMI
        df = norm(df,'plusDI')
        df = norm(df,'minusDI')
        df = norm(df,'DMI')
        #STOCHASTIC
        df = norm(df,'STOCH')
        df = norm(df,'%K')
        df = norm(df,'%D')

        df = norm(df,'RSI')
        df = norm(df,'%R')
    
        x_test = df[['MACD-SL_n','DMI_n','STOCH_n','RSI_n','%R_n']].values
        x_test = add_shift_day(x_test,30)
        y_pred = model.predict(x_test)
        df = df[str(st1)+'-'+str(st2)+'-'+str(st3):]
        y_pred = y_pred[-len(df):]
        df['y_pred'] = PredictThreshold(y_pred)

        df['up'] = np.where(df['y_pred']==0,df['Close'],np.nan)
        df['down'] = np.where(df['y_pred']==1,df['Close'],np.nan)
        df[['Close','up','down']].plot(figsize=(16,10),title=stock[0],color=['blue','green','red'],linewidth=4)
        plt.show()
    except:
        print(stock,'\n','Invalid Stock Name or Date Not Correct')

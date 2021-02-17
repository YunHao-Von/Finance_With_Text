import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
import talib

data=np.array(pd.read_csv("financial_origin_data.csv",encoding="ANSI")[["close","open"]])
datacopy1=data.copy()
datacopy10=data.copy()
datacopy2=data.copy()
m=np.shape(data)[0]
date=np.linspace(0,m-1,m)

def price_means(days,data):
     num=math.floor(m/days)
     n=0
     k=0
     data_sum=0
     for i in range(m):
          if k !=num:
               data_sum=data_sum+data[i]
               n=n+1
               if n==days:
                    data[k*days:k*days+days]=data_sum/days
                    data_sum=0
                    n=0
                    k=k+1
          else:
               break
     return data


if __name__=="__main__":
     fivemeans=price_means(5,data[:,0])
     thirtymeans=price_means(30,datacopy1[:,0])
     tenmeans = price_means(10, datacopy10[:,0])
     plt.figure()
     for i in range(m):
          date_=np.zeros([2])
          date_[0]=i
          date_[1]=i
          gain=np.zeros([2])
          datacopy2=np.sort(datacopy2,axis=0)
          gain[0]=datacopy2[i,1]
          gain[1]=datacopy2[i,0]
          if datacopy2[i,1]<datacopy2[i,0]:
               plt.plot(date_,gain,'r',lw=3)
          else:
               plt.plot(date_,gain,'b',lw=3)
     plt.plot(date,fivemeans[::-1],lw=3,color="orange",label="5MA")
     plt.plot(date,thirtymeans[::-1],lw=3,color="g",label="30MA")
     plt.grid()
     plt.legend()
     plt.title("5MA,30MA",fontsize=20)
     plt.xlabel("Date")
     plt.ylabel("Closing Price")
     plt.show()
     result=pd.read_csv("financial_origin_data.csv",encoding="ANSI")
     processor={
         "5MA":fivemeans,
         "30MA":thirtymeans,
         '10MA':tenmeans
     }
     temp=pd.DataFrame(processor)
     result['5MA']=temp['5MA']
     result['10MA'] = temp['10MA']
     result['30MA'] = temp['30MA']
     result = result.sort_values(by='trade_date', ascending=True)
     close = result['close'].tolist()
     result['MACD'], result['MACDsignal'], result['MACDhist'] = talib.MACD(np.array(close),fastperiod=12, slowperiod=26, signalperiod=9)

     df = pd.read_csv("financial_origin_data.csv", encoding="ANSI")
     df = df.sort_values(by='trade_date', ascending=True)

     dw = pd.DataFrame()
     dw['slowk'], dw['slowd'] = talib.STOCH(
          df['high'].values,
          df['low'].values,
          df['close'].values,
          fastk_period=9,
          slowk_period=3,
          slowk_matype=0,
          slowd_period=3,
          slowd_matype=0)
     # 求出J值，J = (3*K)-(2*D)
     dw['slowj'] = list(map(lambda x, y: 3 * x - 2 * y, dw['slowk'], dw['slowd']))
     dw.index = range(len(dw))
     # 画股票收盘价图
     fig, axes = plt.subplots(2, 1)
     df[['close']].plot(ax=axes[0], grid=True, title="CLose")
     # 画 KDJ 曲线图
     dw[['slowk', 'slowd', 'slowj']].plot(ax=axes[1], grid=True)
     result.to_csv("temp.csv",encoding="ANSI",index=False)
     result=pd.read_csv("temp.csv",encoding="ANSI")
     plt.show()
     result['slowk']=dw['slowk']
     result['slowd'] = dw['slowd']
     result['slowj'] = dw['slowj']
     result.to_csv("Finance.csv",encoding="ANSI",index=False)
     print(result)

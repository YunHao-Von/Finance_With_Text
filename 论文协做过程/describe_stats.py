import pandas as pd
data=pd.read_csv("biyadi.csv",encoding="ANSI")
close=data['close（Y）'].describe()
change=data['change(X2)'].describe()
pct_chg=data['pct_chg(x3)'].describe()
vol=data['vol(X4)'].describe()
MACD=data['MACD(X5)'].describe()
slowj=data['slowj(X6)'].describe()
score=data['score(X7)'].describe()
read=data['read(X8)'].describe()
result  =  pd.DataFrame({ 'close（Y）': close,'change(X2)':change,'pct_chg(x3)':pct_chg,'vol(X4)':vol,
                          'MACD(X5)':MACD,'slowj(X6)':slowj,'score(X7)':score,'read(X8)':read})
result.to_csv("describe.csv",encoding="ANSI")
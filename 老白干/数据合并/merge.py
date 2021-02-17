import pandas as pd
data1=pd.read_csv("Finance.csv",encoding="utf-8")
data2=pd.read_csv("final_result.csv",encoding="utf-8")
print(data1.shape)
print(data2.shape)
result = pd.merge(data1, data2, on='trade_date')
print(result.shape)
result.to_csv("BigHeadCarp.csv",encoding="ANSI",index=False)
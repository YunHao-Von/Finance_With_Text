import pandas as pd
import talib
import matplotlib.pyplot as plt
df =pd.read_csv("financial_origin_data.csv",encoding="ANSI")  # 具体数据与格式见上篇文章
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
fig, axes = plt.subplots(2, 1)
df[['close']].plot(ax=axes[0], grid=True, title="KDJ")
dw[['slowk', 'slowd', 'slowj']].plot(ax=axes[1], grid=True)
plt.show()
print(dw)
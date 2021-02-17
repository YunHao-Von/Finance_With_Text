import tushare as ts
ts.set_token('fff570e8cc0f0b3823254983eb4b48d47dc0f88759a184ae3d021222')
pro = ts.pro_api()
df = pro.daily(ts_code='002594.SZ', start_date='20201209', end_date='20201210')
print(type(df))
print(df)
df.to_csv("jiance.csv",index=False,encoding="ANSI")
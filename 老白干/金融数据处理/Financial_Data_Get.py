import tushare as ts
ts.set_token('fff570e8cc0f0b3823254983eb4b48d47dc0f88759a184ae3d021222')
pro = ts.pro_api()
df = pro.daily(ts_code='600559.sh', start_date='20130312', end_date='20201210')
df.to_csv("financial_origin_data.csv",index=False,encoding="ANSI")
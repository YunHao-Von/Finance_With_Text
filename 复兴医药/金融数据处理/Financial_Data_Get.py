import tushare as ts
ts.set_token('fff570e8cc0f0b3823254983eb4b48d47dc0f88759a184ae3d021222')
pro = ts.pro_api()
df = pro.daily(ts_code='600196.sh', start_date='20200424', end_date='20201211')
df.to_csv("financial_origin_data.csv",index=False,encoding="ANSI")
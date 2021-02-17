import pandas as pd
data = pd.read_csv("result_year.csv" , encoding="ANSI" , low_memory=False)
def weight_mean(group,avg_name,weight_name):
	d=group[avg_name]
	w=group[weight_name].astype('float64')
	try:
		return (d*w).sum() / w.sum()
	except ZeroDivisionError:
		return d.mean()
jiaquan=data.groupby("时间").apply(weight_mean,"新闻","阅读量")
every_sum=data.groupby("时间")['阅读量'].sum().tolist()
dict = {'shijian':jiaquan.index,'score':jiaquan.values,'Read_count':every_sum}
result_1=pd.DataFrame(dict)
result_1.to_csv("result.csv",encoding="ANSI",index=False)
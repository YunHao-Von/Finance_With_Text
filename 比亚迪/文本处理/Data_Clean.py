import pandas as pd
import re
import paddlehub as hub
senta = hub.Module(name="senta_bilstm")
data = pd.read_csv("data.csv",encoding="utf-8",low_memory=False)
data = data.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
newdata = data["read_number"].map(str) + data["fenge1"].map(str) + data["reply_number"].map(str) + data["fenge2"].map(str) + data["titles"].map(str) + data["fenge3"].map(str) + data["dates"].map(str)
result = newdata.str.split('&&&', n=-1, expand=True). \
    rename(columns={0: '阅读量', 1: '回复量', 2: '新闻', 3: '日期'})
temp=result
print(temp)
time = temp.日期.apply(
    lambda x: (re.findall("\d+",x)[0].strip()+re.findall("\d+",x)[1].strip()).strip()
)
temp['日期'] = time
test_text = temp['新闻'].tolist()
score = []
input_dict = {"text": test_text}
results = senta.sentiment_classify(data=input_dict)
for i in results:
    score.append(i['positive_probs'])
temp['新闻'] = score
temp.to_csv("result.csv",encoding="ANSI",index=False)
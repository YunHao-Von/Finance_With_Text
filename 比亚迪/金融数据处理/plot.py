import pandas as pd
plot_data=pd.read_csv("financial_origin_data.csv",encoding="utf-8")
from pyecharts import options as opts
from pyecharts.charts import Kline
plot_data = plot_data.sort_values(by='trade_date', ascending=True)
plot_data.index=range(0,plot_data.shape[0])
#
# x_data = []
# y_data = []
#
# for i in range(0,plot_data.shape[0]):
#     str_date = str(plot_data.iloc[i,1])
#     str_date =str_date[0:4] + "年" + str_date[4:6] + "月" + str_date[6:8]+"日"
#     print(str_date)
#     x_data.append(str_date)
#     y_data.append([plot_data.iloc[i,2],plot_data.iloc[i,3],plot_data.iloc[i,4],plot_data.iloc[i,5]])
# c = (
#     Kline(init_opts=opts.InitOpts(width="1440px", height="800px"))
#     .add_xaxis(xaxis_data=x_data)
#     .add_yaxis(
#         "kline",
#         y_data,
#         itemstyle_opts=opts.ItemStyleOpts(
#             color="#ec0000",
#             color0="#00da3c",
#             border_color="#8A0000",
#             border_color0="#008F28",
#         ),
#     )
#     .set_global_opts(
#         xaxis_opts=opts.AxisOpts(is_scale=True),
#         yaxis_opts=opts.AxisOpts(
#             is_scale=True,
#             splitarea_opts=opts.SplitAreaOpts(
#                 is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
#             ),
#         ),
#         datazoom_opts=[opts.DataZoomOpts(type_="inside")],
#         title_opts=opts.TitleOpts(title="K线走势图"),
#     )
#     .render("plot_changqi_kxian.html")
# )
ma30=plot_data.close.rolling(window=30).mean()
print(len(ma30))
ma30=ma30.dropna(axis=0)
thirty=ma30.tolist()
date=range(1,len(thirty)+1)

from pyecharts.charts import Line
from pyecharts import options
from pyecharts.globals import ThemeType
newdate=[]
for i in range(0,len(date)):
    newdate.append(str(date[i]))
# 1. 准备数据
# cate=newdate
# Confirmed_diagnosis_data=year_rate

# 2. 创建图表对象
line = Line()

# 3. 关联数据
line.add_xaxis(newdate)  # x轴

line.add_yaxis("30MA", thirty,
              # 设置折线是否平滑
              is_smooth=False,is_hover_animation= True,is_symbol_show=False)
# 4. 设置
line.set_series_opts(markline_opts=options.MarkLineOpts(
    # 设置平均值的标记线
    data=[options.MarkPointItem(type_="min", name="最小值"),
          # 设置最大值的标记线
          options.MarkPointItem(type_="max", name="最大值")
          ]))
line.set_global_opts(xaxis_opts=options.AxisOpts(axislabel_opts=options.LabelOpts(rotate=-30)),
                     yaxis_opts=options.AxisOpts(name='每日年化收益率'),
    title_opts=options.TitleOpts(title="每日年化收益率变化曲线",subtitle="副标题"))

# 5. 数据渲染
line.render("plot_changqi_zhexian.html")
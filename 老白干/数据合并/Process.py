import pandas as pd
import numpy as np
data=pd.read_csv("temp.csv",encoding="utf-8")
df_norm2 = data.apply(lambda x: (x - np.mean(x)) / (np.std(x)))
df_norm2.to_csv("temp_result.csv",encoding="ANSI",index=False)
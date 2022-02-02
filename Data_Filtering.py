import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("gravity_data.csv")
for index, data in enumerate(df["Distance"]):
    if(float(data)>100):
        df.drop(index,inplace=True)
del(df["Unnamed: 0"])
df.reset_index(drop=True,inplace=True)
print(df)

for index, data in enumerate(df["gravity"]):
    if(float(data)<150 or float(data)>350  ):
        df.drop(index,inplace=True)
print(df)
df.to_csv("Filtered_Stars.csv",index=False)
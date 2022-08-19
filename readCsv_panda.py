import pandas as pd

df = pd.read_csv("data.csv")

for i in range(5):
    print(df.loc[df.index.size-(i+1)])
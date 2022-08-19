import pandas as pd

df = pd.read_csv("data_2colmns.csv", usecols = ['marks'])
sum = 0
for i in range(df.index.size-1):
    sum = sum+df.loc[i]
print(" mean : ",(sum/df.index.size))

marks = df.values
marks.sort()
mid = len(marks) // 2
res = (marks[mid] + marks[~mid]) / 2
print("Median of list is : ", str(res))


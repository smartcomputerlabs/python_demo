import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model

oecd_bli = pd.read_csv("H:\projects\DataSet\OECD,DF_BLI,+.SW_LIFS..TOT.csv", thousands=',')
gdp_per_capita = pd.read_csv("H:\projects\DataSet\WEOOct2024all.xls",thousands=',',delimiter='\t',encoding='latin1', na_values="n/a")

oecd_bli = oecd_bli[oecd_bli["INEQUALITY"]=="TOT"]
print ("oecd_bli =",oecd_bli)



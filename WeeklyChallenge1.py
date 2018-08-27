import pandas as pd
import numpy as np
import os
print (os.getcwd())
#change working directory
path=r"C:\Users\Nils\Documents\Python"
os.chdir(path)
#import csv files
df_ranges = pd.read_csv("WC_1_Range.csv")
df_stores = pd.read_csv("WC_1_Stores.csv")
#look at data
print (df_ranges.head())
print (df_stores.head())
#form conditions for ranges
conditions =[(df_stores["Postal Area"] >= 2000) & (df_stores["Postal Area"]<=2019),
(df_stores["Postal Area"] >= 2020) & (df_stores["Postal Area"]<=2039),
(df_stores["Postal Area"] >= 2040) & (df_stores["Postal Area"]<=2059),
(df_stores["Postal Area"] >= 2060) & (df_stores["Postal Area"]<=2079),
(df_stores["Postal Area"] >= 2080) & (df_stores["Postal Area"]<=2100)]
# set return values if statements are true
choices = ["2000-2019","2020-2039","2040-2059","2060-2079","2080-2100"]
#apply conditions and choices with select statement
df_stores["Postal Range"] = np.select(conditions,choices)
#inner join on newly created postal code ranges
new_df=pd.merge(df_stores,df_ranges,how="inner", left_on=df_stores["Postal Range"],right_on=df_ranges["Range"])
# group by dimensions and count aggregation
print (new_df.groupby(["Region","Sales Rep","Responder"]).Region.count())

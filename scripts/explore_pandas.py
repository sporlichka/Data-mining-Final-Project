import pandas as pd
import sys

path = sys.argv[1]
cols = ["year","sex","female","age","race","marst","educ99","empstat","classwkr",
        "wkswork1","uhrswork","incwage","hrwage","realhrwage","union","potexp",
        "adj_occ2name","hispan","nativity"]

df = pd.read_csv(path, usecols=cols, low_memory=False)
print("shape:", df.shape)
print()
print("dtypes:\n", df.dtypes)
print()
print("missing per col:\n", df.isna().sum())
print()
print("educ99 value counts:\n", df["educ99"].value_counts(dropna=False).head(15))
print()
print("adj_occ2name value counts:\n", df["adj_occ2name"].value_counts(dropna=False).head(15))
print()
print("incwage describe by sex:\n", df.groupby("sex")["incwage"].describe())
print()
print("realhrwage describe by sex:\n", df.groupby("sex")["realhrwage"].describe())

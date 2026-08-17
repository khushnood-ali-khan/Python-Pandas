import pandas as pd

df = pd.read_excel("C:/Users/This_PC/Desktop/Python/Python-Pandas/Data-Files/university_records.xlsx")

grp = df.groupby('city')

print(grp["cgpa"].max())
print(grp["cgpa"].min())
print(grp["cgpa"].sum())
print(grp["cgpa"].median())
print(grp['city'].count())
print(grp["full_name"].count())

dep = df.groupby("department")
print(dep['department'].count())
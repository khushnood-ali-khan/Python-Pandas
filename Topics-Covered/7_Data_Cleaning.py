import pandas as pd

df = pd.read_csv("C:/Users/This_PC/Desktop/Python/Python-Pandas/Data-Files/ecommerce_orders.csv")

#   DELETE COLUMN
df = df.drop(columns="region")
print(df.to_string())

#   DELETE THE ROWS CONTAINING null VAlUE IN COLUMN
df = df.dropna(subset=["rating"])
print(df.to_string())

#   REPLACE MISSING VALUES
df = df.fillna({"rating": "None"})
print(df.head(200).to_string())

#   FIX INCONSISTENT VALUE
df["category"] = df["category"].replace({"Books" : "Educational"})
print(df.head(100).to_string())

#   MANIPOLATE TEXT
df["category"] = df["category"].str.upper()
print(df.head(50))

#   FIX OR CHANGE DATATYPE / TYPE CONVERSION
df['price'] = df['price'].astype(int)
print(df.head(50))

#   REMOVE DUPLICATES
df = df.drop_duplicates()
print(df)
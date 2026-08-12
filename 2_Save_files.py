import pandas as pd
#   Save Data into files

# Example

data = {
    "Name" : ['Kamran', 'Ali Rahman', 'Asad Nawaz'],
    "Age" : [22, 23, 21]
}

df = pd.DataFrame(data)     #pass the data to panda dataframe

print(df)

df.to_csv("Data_to_csv.csv", index=False)    #save the data as a csv file but would not give defaulte index to data
df.to_excel("Data_to_excel.xlsx")
df.to_json("Data_to_json.json")
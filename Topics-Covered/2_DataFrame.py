import pandas as pd

# DataFrame: DataFrame is a 2 dimensional data structure, like a table with rows and columns

# CREATE A DICTIONARY
data = {
    "Name" : ["Nouman", "Farman", "Farhan", "Shayan"],
    "Age" : [30, 28, 31, 25],
    "Salary" : [100000, 90000, 120000, 140000]
}

# CONVERT DATA INTO DATAFRAME
df = pd.DataFrame(data)
print(df)

# ASSIGN LABELS
df_labels = pd.DataFrame(data, index=["Emp 1", "Emp 2", "Emp 3", "Emp 4"])
print(df_labels)

# ACCESS BY LABEL
print(df_labels.loc['Emp 1'])

# ACCESS BY INDEX NUMBER
print(df_labels.iloc[2])

# ADD A NEW COLUMN
df_labels['Role'] = ["Cyber Security", "Accountent", "Web Dev", "Ai Engineer"]
print(df_labels)

# ADD A NEW ROW
new_row = pd.DataFrame([{
    "Name" : "Shan",
    "Age" : 27,
    "Salary" : 110000,
    "Role"  : "Data Analyis"
}],
index=["Emp 5"])
df_labels = pd.concat([df_labels, new_row])

print(df_labels)
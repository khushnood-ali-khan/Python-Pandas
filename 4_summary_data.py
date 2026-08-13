import pandas as pd

data = pd.read_excel("Data-Files/university_records.xlsx")

print("Display the data info:")

print(data.info())
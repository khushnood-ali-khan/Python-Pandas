import pandas as pd

data = pd.read_excel("C:/Users/This_PC/Desktop/Python/Python-Pandas/Data-Files/university_records.xlsx")

gpa = data[data["cgpa"] > 3.5]
gpa = data[(data['cgpa'] > 3.5) & (data['city'] == "Peshawar")]
city = data[data['city'].isin(['Peshawar', 'Bat Khela'])]
not_department = data[~data["department"].isin(['Business Administration'])]
btw = data[data['cgpa'].between(3.0, 3.5)]

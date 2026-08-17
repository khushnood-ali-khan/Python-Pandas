import pandas as pd

df = pd.read_excel("C:/Users/This_PC/Desktop/Python/Python-Pandas/Data-Files/university_records.xlsx")


# FIND AVERAGE GPA OF THE CLASS
avg = df['cgpa'].mean(numeric_only= True)
print(f"{avg:.2f}")

# FIND MEDIAN(Middle gpa)
mid = df['cgpa'].median(numeric_only=True)
print(mid)

# FIND THE MOST FREQUENT GPA
frequent = df['cgpa'].mode()
print(frequent)

# FIND THE MAXIMUM GPA
maximum = df['cgpa'].max()
print(maximum)

# FIND THE MINIMUN GPA
minimum = df['cgpa'].min()
print(minimum)

# FIND SUM
SUM = df['cgpa'].sum()
print(SUM)

# FIND COUNT
no_count = df['full_name'].count()
print(no_count)

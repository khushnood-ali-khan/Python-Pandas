import pandas as pd

#   READING THE DATA FILE
df = pd.read_excel("C:/Users/This_PC/Desktop/Python/Python-Pandas/Data-Files/university_records.xlsx")
print(df)     #it will print the truncate data(1st and last 5 rows only)

#   TO print the whole data use to_string() function
print(df.to_string())

#   SELECT/PRINT DATA BY COLUMNS
print(df['cgpa'].to_string()) # SINGLE COLUME
print(df[['student_id','full_name', 'cgpa']].to_string())   #  MULTIPLE COLUMNS

#   SELECT/PRINT DATA BY ROWS
print(df.loc[0])                    # This will print a single row on the defualt label
print(df.loc[0:5])                  # Multiple Rows
""" We can also make the column as an index when reading
    like Student ID or there Name to make access easy
"""
new_df = pd.read_excel("C:/Users/This_PC/Desktop/Python/Python-Pandas/Data-Files/university_records.xlsx", index_col="student_id")
#   NOW the student_id will act as an Label instead of defualt index number
print(new_df.to_string())
print(new_df.loc['S2026', ["full_name", "cgpa"]])       # Access through student_id but show only Name and GPA
print(new_df.loc[new_df['cgpa'] < 3])                   # Access throght condition
print(new_df.iloc[0:11])                                #ACCESS first 10 rows on number
print(new_df.iloc[11:31:2])                             #ACCESS every 2nd row from 11 to 31
print(new_df.iloc[0:50:2, 0:4])                         #ACCESS EVERY 2ND ROW FROM 0 to 50 AND SHOW ONLY 0 to 4 COLUMNS
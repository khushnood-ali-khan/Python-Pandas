import pandas as pd

# read excel files
xlsx_df = pd.read_excel("university_records.xlsx")


# using head() and tail()

# head() will load the first rows of the file, by defualt it load first 5
print(xlsx_df.head(10))

# tail() will load the last rows of the file
print(xlsx_df.tail(10))
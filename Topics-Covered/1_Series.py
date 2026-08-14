import pandas as pd

# print(pd.__version__)       # check pandas version

#  Series: One Dimensional array holding data of any type.
#           Like a column in a table

data = ["Kareem", "Nabeel","Shareef","Jameel"]

# series = pd.Series(data)        #converting python list into series (or a column), but without a label or index
# print(series)

series = pd.Series(data, index=['Web Dev', 'Data Analy','Cyber Sec','Ai Eng'])    # PASSING LABELS TO DATA
# print(series.loc['Ai Eng'])         # ACCESSING THE DATA WITH LABEL

# CHANGING THE VALUE
series.loc['Ai Eng'] = "Sameer"
print(series)
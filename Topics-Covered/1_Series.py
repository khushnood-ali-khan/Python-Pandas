import pandas as pd

print(pd.__version__)       # check pandas version

""" Series: One Dimensional array holding data of any type.
            Like a column in a table
"""
data = ["Kareem", "Nabeel","Shareef","Jameel"]

series = pd.Series(data)        #converting python list into series (or a column), but without a label or index
print(series)

# PASSING LABELS TO DATA
series = pd.Series(data, index=['Web Dev', 'Data Analy','Cyber Sec','Ai Eng'])
print(series.loc['Ai Eng'])         # ACCESSING THE DATA WITH LABEL

# CHANGING THE VALUE
series.loc['Ai Eng'] = "Sameer"
print(series)

# ACCESSING THROUGH INDEX NUMBER
print(series.iloc[2])


# RETURN/ACCESS/FILTER BY VALUE
data_list = [100, 104, 108, 112, 116, 120]
list_to_series = pd.Series(data_list, index=['a','b','c','d','e','f'])
print(list_to_series[list_to_series > 110])
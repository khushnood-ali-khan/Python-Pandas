"""
==================================================================
COMPLETE PANDAS CHEAT SHEET
Every line has a comment explaining what it does.
Run sections individually — this file is meant for reference, not
straight execution top-to-bottom (some lines depend on earlier vars).
==================================================================
"""

import pandas as pd          # standard import alias for pandas
import numpy as np           # numpy is commonly used alongside pandas

# ==================================================================
# 1. CREATING DATA STRUCTURES
# ==================================================================

s = pd.Series([1, 2, 3, 4])                          # create a 1D labeled array (Series)
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])      # Series with custom index labels

df = pd.DataFrame({                                   # create a DataFrame from a dict of lists
    'name': ['Ali', 'Sara', 'Zain'],
    'age': [22, 25, 19],
    'city': ['Lahore', 'Karachi', 'Multan']
})

df = pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C'])  # DataFrame from random numpy array

df2 = pd.DataFrame([[1, 2], [3, 4]], columns=['x', 'y'])  # DataFrame from a list of lists

# ==================================================================
# 2. READING & WRITING DATA
# ==================================================================

df = pd.read_csv('file.csv')                          # read a CSV file into a DataFrame
df = pd.read_csv('file.csv', index_col=0)              # read CSV and set first column as index
df = pd.read_excel('file.xlsx', sheet_name='Sheet1')    # read an Excel sheet into a DataFrame
df = pd.read_json('file.json')                          # read a JSON file into a DataFrame
df = pd.read_sql('SELECT * FROM table', con=connection)  # read data from a SQL query
df = pd.read_parquet('file.parquet')                     # read a Parquet file

df.to_csv('out.csv', index=False)                      # write DataFrame to CSV (no row index column)
df.to_excel('out.xlsx', index=False)                    # write DataFrame to Excel file
df.to_json('out.json')                                  # write DataFrame to JSON file
df.to_parquet('out.parquet')                            # write DataFrame to Parquet file

# ==================================================================
# 3. INSPECTING DATA
# ==================================================================

df.head()                 # show first 5 rows
df.head(10)                # show first 10 rows
df.tail()                  # show last 5 rows
df.shape                   # (rows, columns) tuple
df.info()                  # summary: dtypes, non-null counts, memory usage
df.describe()               # summary statistics for numeric columns
df.dtypes                  # data type of each column
df.columns                 # list of column names
df.index                   # index (row labels) of the DataFrame
df.values                  # underlying numpy array of the data
df.memory_usage()           # memory usage of each column
df.nunique()                # number of unique values per column
df.count()                  # count of non-null values per column
df.sample(5)                 # randomly sample 5 rows

# ==================================================================
# 4. SELECTING / INDEXING DATA
# ==================================================================

df['name']                     # select a single column (returns Series)
df[['name', 'age']]              # select multiple columns (returns DataFrame)
df.iloc[0]                      # select row by integer position
df.iloc[0:3]                     # select rows 0 to 2 by position
df.iloc[0, 1]                    # select value at row 0, column 1 by position
df.loc[0]                        # select row by label
df.loc[0:2, 'name']               # select rows 0-2, column 'name' by label
df.loc[df['age'] > 20]              # boolean indexing: rows where age > 20
df.at[0, 'name']                   # fast scalar access by label (single value)
df.iat[0, 1]                       # fast scalar access by integer position
df.query('age > 20')                # select rows using a query string
df.filter(items=['name', 'age'])      # select specific columns by name
df.filter(like='a')                   # select columns whose names contain 'a'
df.filter(regex='^n')                  # select columns matching a regex pattern

# ==================================================================
# 5. FILTERING / BOOLEAN CONDITIONS
# ==================================================================

df[df['age'] > 20]                          # rows where age is greater than 20
df[(df['age'] > 20) & (df['city'] == 'Lahore')]  # multiple conditions (AND)
df[(df['age'] > 20) | (df['age'] < 18)]          # multiple conditions (OR)
df[df['city'].isin(['Lahore', 'Karachi'])]        # rows where city is in a list
df[~df['city'].isin(['Lahore'])]                   # negate a condition (NOT)
df[df['name'].str.contains('a')]                    # rows where string column contains substring
df[df['age'].between(18, 25)]                        # rows where value falls within a range

# ==================================================================
# 6. MODIFYING DATA
# ==================================================================

df['age'] = df['age'] + 1                      # modify an existing column
df['is_adult'] = df['age'] >= 18                 # create a new column from a condition
df['full_info'] = df['name'] + ' - ' + df['city']  # combine columns into a new one
df.rename(columns={'name': 'full_name'})           # rename column(s)
df.rename(index={0: 'first'})                        # rename row index label(s)
df.drop(columns=['city'])                              # drop a column
df.drop(index=[0])                                      # drop a row by index label
df.drop_duplicates()                                     # remove duplicate rows
df.drop_duplicates(subset=['name'])                        # remove duplicates based on specific column
df.reset_index(drop=True)                                   # reset index to default integers
df.set_index('name')                                          # set a column as the new index
df.sort_values('age')                                           # sort rows by column value (ascending)
df.sort_values('age', ascending=False)                            # sort descending
df.sort_index()                                                     # sort rows by index
df.T                                                                 # transpose rows and columns

# ==================================================================
# 7. HANDLING MISSING DATA
# ==================================================================

df.isnull()                       # boolean DataFrame: True where value is NaN
df.isnull().sum()                   # count of missing values per column
df.notnull()                         # boolean DataFrame: True where value is NOT NaN
df.dropna()                           # drop rows with any missing values
df.dropna(axis=1)                       # drop columns with any missing values
df.dropna(how='all')                     # drop rows only if ALL values are missing
df.fillna(0)                               # fill missing values with 0
df.fillna(df.mean(numeric_only=True))        # fill missing values with column mean
df.fillna(method='ffill')                      # forward-fill missing values
df.fillna(method='bfill')                        # backward-fill missing values
df.interpolate()                                   # fill missing values using interpolation

# ==================================================================
# 8. GROUPING & AGGREGATION
# ==================================================================

df.groupby('city')                                  # group DataFrame by column values
df.groupby('city').mean(numeric_only=True)             # mean of each group
df.groupby('city')['age'].sum()                           # sum of 'age' per group
df.groupby('city').agg({'age': 'mean', 'name': 'count'})     # multiple aggregations per column
df.groupby(['city', 'is_adult']).size()                        # group by multiple columns, count rows
df.groupby('city').apply(lambda x: x['age'].max())               # custom aggregation function
df.pivot_table(values='age', index='city', aggfunc='mean')         # pivot table with aggregation
df.pivot(index='name', columns='city', values='age')                 # reshape data (pivot)

# ==================================================================
# 9. MERGING / JOINING / CONCATENATING
# ==================================================================

pd.concat([df, df2], axis=0)                          # stack DataFrames vertically (row-wise)
pd.concat([df, df2], axis=1)                            # stack DataFrames horizontally (column-wise)
pd.merge(df, df2, on='id')                                # SQL-style inner join on a common column
pd.merge(df, df2, on='id', how='left')                       # left join (keep all rows from df)
pd.merge(df, df2, on='id', how='right')                        # right join (keep all rows from df2)
pd.merge(df, df2, on='id', how='outer')                          # outer join (keep all rows from both)
df.join(df2, how='left')                                            # join on index instead of column

# ==================================================================
# 10. APPLYING FUNCTIONS
# ==================================================================

df['age'].apply(lambda x: x * 2)                    # apply function to each value in a column
df.apply(lambda row: row['age'] + 1, axis=1)          # apply function across each row
df.applymap(lambda x: str(x))                           # apply function to every element in DataFrame
df['name'].map({'Ali': 'A', 'Sara': 'S'})                  # map values using a dictionary
df['name'].str.upper()                                       # convert strings to uppercase
df['name'].str.lower()                                         # convert strings to lowercase
df['name'].str.strip()                                           # remove leading/trailing whitespace
df['name'].str.replace('a', 'A')                                   # replace substring in strings
df['name'].str.split(' ')                                            # split strings into lists
df['name'].str.len()                                                   # length of each string

# ==================================================================
# 11. DATE & TIME HANDLING
# ==================================================================

df['date'] = pd.to_datetime(df['date'])              # convert column to datetime type
df['year'] = df['date'].dt.year                        # extract year from datetime column
df['month'] = df['date'].dt.month                        # extract month from datetime column
df['day'] = df['date'].dt.day                              # extract day from datetime column
df['weekday'] = df['date'].dt.day_name()                      # get name of weekday
pd.date_range(start='2024-01-01', periods=5, freq='D')           # generate a range of dates
df.set_index('date').resample('M').mean(numeric_only=True)         # resample time series data monthly

# ==================================================================
# 12. STATISTICS & MATH
# ==================================================================

df['age'].mean()               # average value
df['age'].median()               # median value
df['age'].mode()                   # most frequent value
df['age'].std()                      # standard deviation
df['age'].var()                        # variance
df['age'].min()                          # minimum value
df['age'].max()                            # maximum value
df['age'].sum()                              # sum of values
df['age'].cumsum()                             # cumulative sum
df['age'].corr(df['age'])                        # correlation between two columns
df.corr(numeric_only=True)                          # correlation matrix of numeric columns
df['age'].value_counts()                              # frequency count of unique values

# ==================================================================
# 13. RESHAPING DATA
# ==================================================================

df.melt(id_vars=['name'], value_vars=['age'])       # unpivot columns into rows (wide to long)
df.stack()                                             # pivot columns into rows (compress)
df.unstack()                                             # pivot rows into columns (expand)
df.explode('name')                                         # expand list-like column into multiple rows

# ==================================================================
# 14. WORKING WITH DUPLICATES & UNIQUE VALUES
# ==================================================================

df.duplicated()                       # boolean Series: True for duplicate rows
df['name'].unique()                     # array of unique values in a column
df['name'].nunique()                      # count of unique values in a column

# ==================================================================
# 15. OPTIONS & DISPLAY SETTINGS
# ==================================================================

pd.set_option('display.max_rows', 100)      # set max number of rows to display
pd.set_option('display.max_columns', 50)      # set max number of columns to display
pd.set_option('display.width', 1000)            # set console display width
pd.reset_option('all')                            # reset all display options to default

# ==================================================================
# 16. COPYING & TYPE CONVERSION
# ==================================================================

df_copy = df.copy()                    # create a deep copy (avoid modifying original)
df['age'] = df['age'].astype(float)      # convert column data type to float
df['age'] = df['age'].astype(int)          # convert column data type to int
df['name'] = df['name'].astype(str)          # convert column data type to string
df['city'] = df['city'].astype('category')     # convert column to category dtype (saves memory)

import pandas as pd

# read csv files with pandas
csv_df = pd.read_csv("Data-Files/ecommerce_orders.csv")

# read json files
json_df = pd.read_json("Data-Files/employees.json")

# read excel files
xlsx_df = pd.read_excel("Data-Files/university_records.xlsx")


# to read data from cloud storage use gcsfs  library
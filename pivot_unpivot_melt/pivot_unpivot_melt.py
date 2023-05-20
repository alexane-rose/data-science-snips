# Plot transactions using plotly
## 1. Reads data from output/data/deribit_trades.csv (run Make get_data)
## 2. Pivots a table, reindexes it and formats the columns
## 3. Melts data to retireve the original format

import pandas as pd
import plotly.express as px
import os
import numpy as np

## 1. Reads data from output/data/deribit_trades.csv (run Make get_data)
# Get Data
input_dir = f"{os.getcwd()}/output/data/deribit_trades.csv"
print(input_dir)

# Read data
df = pd.read_csv(input_dir)
df["year"] = pd.to_datetime(df["timestamp"], unit="us").dt.year
df["month"] = pd.to_datetime(df["timestamp"], unit="us").dt.month
df["day"] = pd.to_datetime(df["timestamp"], unit="us").dt.day
df["hour"] = pd.to_datetime(df["timestamp"], unit="us").dt.hour
print("Original Table : ")
print(df.head())
print("-----------------------------------")


## 2. Pivots a table, reindexes it and formats the columns
# Pivot the table
df_pivot = pd.pivot_table(
    df,
    index=["year", "month", "day", "hour", "symbol"],
    columns="side",
    values=["price", "amount"],
    aggfunc={"price": np.mean, "amount": np.mean},
).reset_index()

# Format columns for pivot table
consolidated_headers = [
    " ".join(col).strip().replace(" ", "_") for col in df_pivot.columns
]
print(f"New column names : {consolidated_headers}")
df_pivot.columns = consolidated_headers
print(f"New pivot table: ")
print(df_pivot.head(6))
print("-----------------------------------")


## 3. Melts data to retrieve the original format
# Get value columns
value_columns = ["amount", "price"]
id_columns = df_pivot.columns[
    ~df_pivot.columns.str.contains("|".join(value_columns))
].to_list()

frames = []

for val in value_columns:
    val_columns = df_pivot.columns[df_pivot.columns.str.contains(val)]
    df_melt_val = pd.melt(
        df_pivot,
        id_vars=id_columns,
        value_vars=val_columns,
        var_name="side",
        value_name=val,
    )
    df_melt_val["side"] = df_melt_val["side"].str.replace(f"{val}_", "")
    frames.append(df_melt_val)

id_columns.append("side")
df_restored = pd.merge(frames[0], frames[1], on=id_columns)
print("Restored Table (aggregated data) : ")
print(df_restored.head(6))

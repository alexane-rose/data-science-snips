# Plot transactions using plotly
## 1. Reads data from output/data/deribit_trades.csv (run Make get_data)
## 2. Scales target columns
## 3. Restores original data

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
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

# Scale target columns
scaling_columns = ['price','amount']
scaler = MinMaxScaler()
df_scaled = df.copy()
df_scaled[scaling_columns] = scaler.fit_transform(df_scaled[scaling_columns])
print("Scaled Table : ")
print(df_scaled.head())
print("-----------------------------------")

# Restore original values
df_restored = df_scaled.copy()
df_restored[scaling_columns] = scaler.inverse_transform(df_scaled[scaling_columns])
print("Restored Table : ")
print(df_scaled.head())
print("-----------------------------------")

# Encoding transaction data
## 1. Reads data from output/data/deribit_trades.csv (run Make get_data)
## 2.

import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import os
import numpy as np
import category_encoders as ce  # noqa: E402

from encoding_lib import get_encoder

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

# Encode Table
encoding_dict = {}
ecoding_methods = ["Binary", "One_hot", "Ordinal", "Hashing"]

for method in ecoding_methods:
    encoder = get_encoder(method, df)
    encoded_df = encoder.transform(df)
    encoding_dict[method] = {"encoder": encoder, "data_frame": encoded_df}
print(encoding_dict)

# Reverse Encode

for method in ecoding_methods:
    if method.upper() != "HASHING":
        encoder = encoding_dict[method]["encoder"]
        restored_df = encoder.inverse_transform(encoding_dict[method]["data_frame"])
        print(f"Inverse transform from : {method}")
        print(restored_df.head(6))
    else :
        print("No inverse transform for hashing")

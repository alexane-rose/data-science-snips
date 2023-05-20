# Plot transactions using plotly
## 1. Reads data from output/data/deribit_trades.csv (run Make get_data)
## 2. Creates scatter plot
## 3. Saves plot to png

import pandas as pd
import plotly.express as px
import os

# Get Data
input_dir = f"{os.getcwd()}/output/data/deribit_trades.csv"
print(input_dir)

# Read data
df = pd.read_csv(input_dir)
print(df.head())
print(df.describe())
# Create scatter chart
fig = px.scatter(df, x="timestamp", y="price", color="amount")

# Write chart
# Check if the directory exists
output_dir = f"{os.getcwd()}/output/fig"
if not os.path.exists(output_dir):
    # If it doesn't exist, create it
    os.makedirs(output_dir)
fig.write_image(f"{output_dir}/transaction_scatter_plotly.png")

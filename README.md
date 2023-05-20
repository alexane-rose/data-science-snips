# data-science-snips
Snips and examples to help build data science projects ✂️

# Running the repo
After cloning the repo, fetch the dataset by running the make target.
`make get_data`
or the curl command
`curl -o output/data/deribit_trades.csv.gz https://datasets.tardis.dev/v1/deribit/trades/2019/11/01/BTC-PERPETUAL.csv.gz`
All examples in this repo rely on this table.

To install required libraries run
`make init`
or the command
`pip install -r requirements.txt`

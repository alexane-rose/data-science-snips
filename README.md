# data-science-snips
Snips and examples to help build data science projects ✂️

# Running the repo
After cloning the repo, fetch the dataset by running the make target.
`make get_data`
or the curl command :

`curl -o output/data/deribit_trades.csv.gz https://datasets.tardis.dev/v1/deribit/trades/2019/11/01/BTC-PERPETUAL.csv.gz`

All examples in this repo rely on this table.


To install required libraries run:

`make init`

or the command

`pip install -r requirements.txt`


Some directories require additional libraries, a `requirements.txt` file is available within the directory to fetch the remaining modules.

# What you will find
In this repository you will find functions that are handy and regularly used when working on data science projects in python.
- encoding_data : methods to encode categorical values
- pivot_unpivot_melt : methods to pivot data and melt data. Pivot is useful when taking raw data and wanting to make it more reader-friendly. Melt is useful in the reverse scenario, when processing a reader-friendly data-set and making it machine-friendly.
- plot_using_plotly : Plotly is great to create interractive visuals. They can be saved to pictures or to HTML
- scaling_data : Scaling data is a necessary step when working with Neuronal networks, it helps the machine converge towards a result!

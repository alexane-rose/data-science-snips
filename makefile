get_data:
	mkdir -p output/data
	curl -o output/data/deribit_trades.csv.gz https://datasets.tardis.dev/v1/deribit/trades/2019/11/01/BTC-PERPETUAL.csv.gz
	gzip -d output/data/deribit_trades.csv.gz

init :
	pip install -r requirements.txt

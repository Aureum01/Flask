# advanced rest api for finance
from flask import Flask, request, jsonify
import requests
import yfinance as yf

app = Flask(__name__)

# A route to get stock info for a single ticker
@app.route('/stock/<string:ticker>', methods=['GET'])
def get_stock_info(ticker):
    stock = yf.Ticker(ticker)
    data = stock.info
    return jsonify(data)

# A route to get stock history for a single ticker
@app.route('/stock/<string:ticker>/history', methods=['GET'])
def get_stock_history(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period='max')
    return jsonify(data)

# A route to get stock info for multiple tickers
@app.route('/stocks', methods=['POST'])
def get_multi_stock_info():
    # Get the list of tickers from the request body
    tickers = request.json['tickers']

    # Get stock info for each ticker
    stocks = []
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        data = stock.info
        stocks.append(data)

    return jsonify({'stocks': stocks})

# A route to perform analysis on stock data
@app.route('/stocks/analyze', methods=['POST'])
app = Flask(__name__)

# A route to get stock info for a single ticker
@app.route('/stock/<string:ticker>', methods=['GET'])
def get_stock_info(ticker):
    stock = yf.Ticker(ticker)
    data = stock.info
    return jsonify(data)

# A route to get stock history for a single ticker
@app.route('/stock/<string:ticker>/history', methods=['GET'])
def get_stock_history(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period='max')
    return jsonify(data)

# A route to get stock info for multiple tickers
@app.route('/stocks', methods=['POST'])
def get_multi_stock_info():
    # Get the list of tickers from the request body
    tickers = request.json['tickers']

    # Get stock info for each ticker
    stocks = []
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        data = stock.info
        stocks.append(data)

    return jsonify({'stocks': stocks})

# A route to perform analysis on stock data
@app.route('/stocks/analyze', methods=['POST'])
def analyze_stocks():
    # Get the list of tickers and analysis type from the request body
    tickers = request.json['tickers']
    analysis_type = request.json['analysis_type']

    # Perform the specified analysis on each ticker
    results = []
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        data = stock.history(period='max')

        if analysis_type == 'mean_close_price':
            result = data['Close'].mean()
        elif analysis_type == 'max_volume':
            result = data['Volume'].max()
        else:
            result = 'Invalid analysis type'

        results.append({'ticker': ticker, 'result': result})

    return jsonify({'results': results})

if __name__ == '__main__':
    app.run()

# Get stock info for Apple
#curl http://localhost:5000/stock/AAPL

# Get stock history for Google
# curl http://localhost:5000/stock/GOOGL/history

# Get stock info for multiple tickers
# curl -X POST -H "Content-Type: application/json" -d '{"tickers": ["AAPL", "GOOGL"]}' http://localhost:5000/stocks

# Perform analysis on stock data
# curl -X POST -H "Content-Type: application/json" -d '{"tickers": ["AAPL", "GOOGL"], "analysis_type": "mean_close_price"}' http://localhost:5000/stocks/analyze


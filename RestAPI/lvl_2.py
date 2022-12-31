#access online stock data
# pip install flask requests yfinance
from flask import Flask, jsonify
import requests
import yfinance as yf

app = Flask(__name__)

@app.route('/stock/<string:ticker>', methods=['GET'])
def get_stock_info(ticker):
    stock = yf.Ticker(ticker)
    data = stock.info
    return jsonify(data)

@app.route('/stock/<string:ticker>/history', methods=['GET'])
def get_stock_history(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period='max')
    return jsonify(data)
if __name__ == '__main__':
    app.run()

# Get stock info for Apple
# curl http://localhost:5000/stock/AAPL

# Get stock history for Google
# curl http://localhost:5000/stock/GOOGL/history

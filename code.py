import yfinance as yf
import pandas as pd
import numpy as np

# Fetch historical data
def get_historical_data(symbol, start="2024-01-01", end="2024-10-30", interval="1d"):
    stock_data = yf.download(symbol, start=start, end=end, interval=interval)
    return stock_data

# Strategy calculations
def calculate_signals(data):
    # Moving Average Crossover
    data['SMA_short'] = data['Close'].rolling(window=20).mean()
    data['SMA_long'] = data['Close'].rolling(window=50).mean()
    data['MA_Signal'] = np.where(data['SMA_short'] > data['SMA_long'], "buy", "sell")

    # RSI Calculation
    delta = data['Close'].diff(1)
    gain = delta.where(delta > 0, 0).rolling(window=14).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=14).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    data['RSI_Signal'] = np.where(data['RSI'] < 30, "buy", np.where(data['RSI'] > 70, "sell", "hold"))

    # MACD Calculation
    data['EMA_short'] = data['Close'].ewm(span=12, adjust=False).mean()
    data['EMA_long'] = data['Close'].ewm(span=26, adjust=False).mean()
    data['MACD'] = data['EMA_short'] - data['EMA_long']
    data['Signal_line'] = data['MACD'].ewm(span=9, adjust=False).mean()
    data['MACD_Signal'] = np.where(data['MACD'] > data['Signal_line'], "buy", "sell")

    # Final recommendation
    data['Buy_Score'] = (data['MA_Signal'] == "buy").astype(int) + \
                        (data['RSI_Signal'] == "buy").astype(int) + \
                        (data['MACD_Signal'] == "buy").astype(int)
    data['Sell_Score'] = (data['MA_Signal'] == "sell").astype(int) + \
                         (data['RSI_Signal'] == "sell").astype(int) + \
                         (data['MACD_Signal'] == "sell").astype(int)

    data['Recommendation'] = np.where(data['Buy_Score'] > data['Sell_Score'], "buy",
                                      np.where(data['Sell_Score'] > data['Buy_Score'], "sell", "hold"))
    return data

# Example usage
data = get_historical_data("NIFTYBEES.NS")  
data = calculate_signals(data)

# Display final recommendation
print(data[['SMA_short', 'SMA_long', 'RSI', 'MACD', 'Signal_line', 'MA_Signal', 'RSI_Signal', 'MACD_Signal', 'Recommendation']].tail())

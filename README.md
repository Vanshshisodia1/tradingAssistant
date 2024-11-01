Here’s a description of our project, along with essential details:

### Project Title
**Trading Assistant for Stock Recommendations**

### Description
This project is a trading assistant tool that provides stock recommendations ("buy," "sell," or "hold") based on technical indicators using Yahoo Finance data. It assists users by analyzing historical data and identifying trade signals without automating trades.

### Key Features
- **Data Source**: Yahoo Finance via `yfinance` API.
- **Indicators Used**:
  - **Moving Average Crossover**: Detects trends with 20-day and 50-day SMAs.
  - **RSI (Relative Strength Index)**: Identifies overbought and oversold conditions.
  - **MACD (Moving Average Convergence Divergence)**: Confirms momentum and trend shifts.
- **Final Recommendation**: Combines all indicators to suggest trade action.
  
### Usage
1. Users can select a stock by ticker symbol (e.g., `RELIANCE.NS`).
2. The program calculates indicators based on historical price data.
3. It outputs a recommendation to assist in making trade decisions.

### Installation Requirements
- Python libraries: `yfinance`, `pandas`, and `numpy`

### How It Works
The assistant uses daily historical data to compute SMAs, RSI, and MACD for selected stocks. Each indicator generates a signal ("buy" or "sell"), and the final recommendation is based on the majority signal from these strategies.

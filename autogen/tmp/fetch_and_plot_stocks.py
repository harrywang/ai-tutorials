# filename: fetch_and_plot_stocks.py
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Define the tickers and the start date of the year
tickers = ['TSLA', 'META']
start_date = '2024-01-01'
end_date = '2024-04-13'  # Today's date

# Fetch historical data from Yahoo Finance
data = yf.download(tickers, start=start_date, end=end_date)

# Calculate the price gains (% change from year start)
starting_prices = data['Adj Close'].iloc[0]
gains = (data['Adj Close'] - starting_prices) / starting_prices * 100

# Plotting the gains
plt.figure(figsize=(10, 6))
plt.plot(gains.index, gains['TSLA'], label='TSLA YTD Gain %')
plt.plot(gains.index, gains['META'], label='META YTD Gain %')
plt.title('TSLA vs META Stock Price Gains YTD (2024)')
plt.xlabel('Date')
plt.ylabel('Percentage Gain')
plt.legend()
plt.grid(True)

# Save the plot to a file
plt.savefig('stock_gains.png')
plt.close()

print("Stock gains plotted and saved to 'stock_gains.png'")
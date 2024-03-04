import pandas as pd
import matplotlib.pyplot as plt
from logic import nadaraya_watson_envelope, find_signals

def plot():
    """
    Plots the closing price of a stock, its Nadaraya-Watson smoothed curve,
    upper and lower envelopes, and buy/sell signals based on the crossing
    of the price with these envelopes.
    
    The data is loaded from a CSV file named 'data.csv', which should contain
    at least two columns: Date and Close, where 'Date' is in YYYY-MM-DD format.
    
    The resulting plot is saved as 'image.png' in the current working directory.
    """
    # Load and prepare the dataset
    df = pd.read_csv('data.csv')
    df['Date'] = pd.to_datetime(df['Date'])  # Ensure the 'Date' column is datetime type

    # Apply the Nadaraya-Watson function to smooth the series and compute envelopes
    src = df['Close'].values
    smoothed, upper, lower = nadaraya_watson_envelope(src)

    # Identify buy and sell signals based on the series and envelopes
    buy_signals, sell_signals = find_signals(src, upper, lower)

    # Set up the plot
    plt.figure(figsize=(14, 7))
    plt.plot(df['Date'], src, label='Close Price', color='gray')
    plt.plot(df['Date'], smoothed, label='Nadaraya-Watson Smoothed', color='blue')
    plt.plot(df['Date'], upper, label='Upper Envelope', color='green')
    plt.plot(df['Date'], lower, label='Lower Envelope', color='red')
    plt.fill_between(df['Date'], lower, upper, color='green', alpha=0.1)  # Highlight the area between envelopes

    # Highlight buy and sell signals on the plot
    plt.scatter(df['Date'][buy_signals], df['Close'][buy_signals], label='Buy Signal', marker='^', color='lime', s=100)
    plt.scatter(df['Date'][sell_signals], df['Close'][sell_signals], label='Sell Signal', marker='v', color='red', s=100)

    # Finalize the plot
    plt.title('Nadaraya-Watson Envelope Indicator with Signals')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.xticks(rotation=45)  # Improve date readability
    plt.tight_layout()

    # Save the plot
    plt.savefig('image.png')

import pandas as pd
import matplotlib.pyplot as plt
from logic import nadaraya_watson_envelope, find_signals

def plot():
    # Load the dataset
    df = pd.read_csv('data.csv')
    df['Date'] = pd.to_datetime(df['Date'])

    # Apply the Nadaraya-Watson function
    src = df['Close'].values
    smoothed, upper, lower = nadaraya_watson_envelope(src)

    # Find buy and sell signals
    buy_signals, sell_signals = find_signals(src, upper, lower)

    # Plot
    plt.figure(figsize=(14, 7))
    plt.plot(df['Date'], src, label='Close Price', color='gray')
    plt.plot(df['Date'], smoothed, label='Nadaraya-Watson Smoothed', color='blue')
    plt.plot(df['Date'], upper, label='Upper Envelope', color='green')
    plt.plot(df['Date'], lower, label='Lower Envelope', color='red')
    plt.fill_between(df['Date'], lower, upper, color='green', alpha=0.1)

    # Plot buy signals
    plt.scatter(df['Date'][buy_signals], df['Close'][buy_signals], label='Buy Signal', marker='^', color='lime', s=100)

    # Plot sell signals
    plt.scatter(df['Date'][sell_signals], df['Close'][sell_signals], label='Sell Signal', marker='v', color='red', s=100)

    plt.title('Nadaraya-Watson Envelope Indicator with Signals')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot as an image file
    plt.savefig('image.png')


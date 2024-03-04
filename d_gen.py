import pandas as pd
import numpy as np

def d_gen():
    # random seed
    dates = pd.date_range(start='2023-01-01', end='2024-01-31', freq='D')
    prices = np.cumsum(np.random.randn(len(dates))) + 100  # Simulate random walk starting at 100

    # Create a DataFrame
    df = pd.DataFrame({'Date': dates, 'Close': prices})

    # Save the data to a CSV file
    df.to_csv('data.csv', index=False)

    df.head()


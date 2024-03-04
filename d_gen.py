# Import necessary libraries
import pandas as pd
import numpy as np

def d_gen():
    """
    Generates a DataFrame containing simulated daily closing prices for a given date range,
    and saves this data to a CSV file. The simulated prices follow a random walk starting at 100.
    
    Outputs:
        Saves the generated DataFrame to 'data.csv' in the current directory.
        Returns the head of the DataFrame for quick inspection.
    """
    # Generate a range of dates from 2023-01-01 to 2024-01-31
    dates = pd.date_range(start='2023-01-01', end='2024-01-31', freq='D')
    
    # Simulate random walk for closing prices starting at 100
    prices = np.cumsum(np.random.randn(len(dates))) + 100

    # Create DataFrame with dates and closing prices
    df = pd.DataFrame({'Date': dates, 'Close': prices})

    # Save the DataFrame to a CSV file without the index
    df.to_csv('data.csv', index=False)

    # Return the first five rows of the DataFrame for inspection
    return df.head()

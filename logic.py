import numpy as np

def gauss_kernel(x, h):
    """
    Computes the Gaussian kernel for a given distance and bandwidth.
    
    Parameters:
        x (float): The distance between points.
        h (float): The bandwidth parameter controlling the smoothness.
    
    Returns:
        float: The computed Gaussian kernel value.
    """
    return np.exp(-0.5 * (x / h) ** 2) / (h * np.sqrt(2 * np.pi))

def nadaraya_watson_envelope(series, bandwidth=8, mult=3):
    """
    Applies the Nadaraya-Watson estimator to smooth a given series and calculate
    the upper and lower envelope based on a specified multiple of deviation.
    
    Parameters:
        series (np.array): The input data series to be smoothed.
        bandwidth (int, optional): The bandwidth parameter for the kernel. Defaults to 8.
        mult (int, optional): The multiple of deviation used to calculate the envelopes. Defaults to 3.
    
    Returns:
        tuple: A tuple containing the smoothed series, upper envelope, and lower envelope.
    """
    n = len(series)
    weights = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            weights[i, j] = gauss_kernel(i - j, bandwidth)
            
    den = weights.sum(axis=1)
    smoothed = np.dot(weights, series) / den
    
    deviation = mult * np.mean(np.abs(series - smoothed))
    upper = smoothed + deviation
    lower = smoothed - deviation
    
    return smoothed, upper, lower

def find_signals(src, upper, lower):
    """
    Identifies potential buy and sell signals based on the source data crossing
    the calculated upper and lower envelopes.
    
    Parameters:
        src (np.array): The original data series.
        upper (np.array): The upper envelope series.
        lower (np.array): The lower envelope series.
    
    Returns:
        tuple: A tuple of two arrays indicating buy signals and sell signals, respectively.
    """
    buy_signals = src < lower  # Condition for potential buy signal
    sell_signals = src > upper  # Condition for potential sell signal
    return buy_signals, sell_signals

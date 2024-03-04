import numpy as np

# Kernel function
def gauss_kernel(x, h):
    return np.exp(-0.5 * (x / h) ** 2) / (h * np.sqrt(2 * np.pi))

# Nadaraya-Watson function
def nadaraya_watson_envelope(series, bandwidth=8, mult=3):
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

# Function to find buy and sell signals
def find_signals(src, upper, lower):
    buy_signals = src < lower  # Condition for potential buy signal
    sell_signals = src > upper  # Condition for potential sell signal
    return buy_signals, sell_signals

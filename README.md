# Nadaraya-Watson Envelope Indicator Analysis
****Overview****
This project applies the Nadaraya-Watson Envelope Indicator to financial market data to identify potential buy and sell signals based on stock price movements. It includes a Python-based analysis pipeline that loads historical stock prices, applies the Nadaraya-Watson smoothing technique to identify trends, and visualizes these trends with potential trading signals.

**Features**
Data Preparation: Load and preprocess historical stock price data.
Smoothing and Envelope Calculation: Apply the Nadaraya-Watson estimator to smooth price data and calculate upper and lower envelopes.
Signal Detection: Identify potential buy and sell signals based on price interactions with the envelopes.
Visualization: Generate and save visual representations of the price data, smoothing effects, and identified signals.

![image](https://github.com/rcc00n/CryptoBot/assets/123768783/d4929320-2c52-4c04-805d-589bd626499b)


*Getting Started*
**Prerequisites**
Ensure you have Python 3.x installed on your system along with the following packages:
- pandas
- numpy
- matplotlib
- Installation

** Clone the repository to your local machine: **

git clone https://github.com/your-username/your-repository.git
cd your-repository

**Usage**
1. Data Preparation: Place your CSV file named data.csv in the project directory. The CSV file should contain at least two columns: Date and Close, where Date is in YYYY-MM-DD format.
2. Running the Analysis:
Execute the main script to perform the analysis and generate the output plot: This will create an image file image.png in the project directory, showcasing the stock price, smoothed price curve, envelopes, and buy/sell signals.

**Documentation**
- logic.py: Contains the core functions for the analysis, including the Nadaraya-Watson envelope calculation and signal detection logic.
- main.py: The entry point of the program. It orchestrates the data loading, analysis, and plotting.

**Contributing**
Contributions to improve the project are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Commit your changes (git commit -am 'Add some feature').
4. Push to the branch (git push origin feature-branch).
5. Create a new Pull Request.

**License**
This project is licensed under the GPL 3.0 License - see the LICENSE file for details.

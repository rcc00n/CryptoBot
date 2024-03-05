from d_gen import d_gen
from plot import plot
from backtest import run_backtests, analyze_results


    

if __name__ == '__main__':
    results = run_backtests()
    analyze_results(results)
    d_gen()
    plot()
    

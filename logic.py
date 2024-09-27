n = 2  # Number of periods. This could be adjusted based on the user's input

def find_fractals(data):
    data['Up Fractal'] = False
    data['Down Fractal'] = False
    down_fract = set()
    up_fract = set()


    for i in range(1, len(data) - 1):
        if data['High'][i] > data['High'][i - 1] and data['High'][i] >
data['High'][i + 1]:
            down_fract.add(i)
        if data['Low'][i] < data['Low'][i - 1] and data['Low'][i] <
data['Low'][i + 1]:
            up_fract.add(i)
    return up_fract, down_fract, 

def garbage_collector_down_fract(data, down_fract):
    # Sort down_fract based on 'High' values at these indices, keeping only the top 2
    if len(down_fract) > 2:
        # Use a temporary list to sort the fractals by their 'High' values in descending order
        sorted_fractals = sorted(down_fract, key=lambda x: data['High'][x], reverse=True)
        # Keep only the top 2 fractals with the highest 'High' values
        return set(sorted_fractals[:2])
    else:
        return down_fract

def garbage_collector_up_fract(data, up_fract):
    # Sort up_fract based on 'Low' values at these indices, keeping only the bottom 2
    if len(up_fract) > 2:
        # Use a temporary list to sort the fractals by their 'Low' values in ascending order
        sorted_fractals = sorted(up_fract, key=lambda x: data['Low'][x])
        # Keep only the bottom 2 fractals with the lowest 'Low' values
        return set(sorted_fractals[:2])
    else:
        return up_fract
def find_signals():
    
buy_signals = up_fract 
sell_signals = down_fract

return buy_signals, sell_signals 

    
    

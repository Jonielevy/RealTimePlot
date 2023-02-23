import random
from itertools import count
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

x_vals = []
y1_vals = []
y2_vals = []
fft_vals = []

index = count()

def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    y1_vals.append(y1.iloc[-1])
    y2_vals.append(y2.iloc[-1])
    x_vals.append(x.iloc[-1])
    
    if len(y1_vals) > 50:
        y1_vals.pop(0)
        y2_vals.pop(0)
        x_vals.pop(0)
    
    # Perform FFT on latest data
    y1_fft = np.fft.fft(y1_vals)
    y2_fft = np.fft.fft(y2_vals)
    fft_vals.append((y1_fft, y2_fft))
    
    if len(fft_vals) > 50:
        fft_vals.pop(0)
    
    plt.clf()
    
    plt.subplot(3, 1, 1)
    plt.plot(x_vals, y1_vals, label='Channel 1')
    plt.legend(loc='upper left')
    plt.title('Channel 1')
    plt.xlabel('Time[s]')
    plt.ylabel('Measurement_1')
    plt.style.use('fivethirtyeight')
    
    plt.subplot(3, 1, 2)
    plt.plot(x_vals, y2_vals, label='Channel 2')
    plt.legend(loc='upper left')
    plt.title('Channel 2')
    plt.xlabel('Time[s]')
    plt.ylabel('Measurement_2')
    plt.style.use('Solarize_Light2')
    
    plt.subplot(3, 1, 3)
    plt.plot(np.abs(fft_vals[-1][0]), label='Channel 1')
    plt.plot(np.abs(fft_vals[-1][1]), label='Channel 2')
    plt.legend(loc='upper left')
    plt.title('FFT')
    plt.xlabel('Frequency')
    plt.ylabel('Magnitude')
    plt.ylim(0, 2000000)
    
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=100)

plt.show()

import serial
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with the port your Arduino is connected to
ser.flushInput()

x_vals = []
y1_vals = []
y2_vals = []
y3_vals = []
fft_vals = [[], [], []]

def animate(i):
    # Read data from the Arduino's serial port
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        data = list(map(int, line.split(',')))
        x = data[0]
        y1 = data[1]
        y2 = data[2]
        y3 = data[3]

        y1_vals.append(y1)
        y2_vals.append(y2)
        y3_vals.append(y3)
        x_vals.append(x)

        if len(y1_vals) > 50:
            y1_vals.pop(0)
            y2_vals.pop(0)
            y3_vals.pop(0)
            x_vals.pop(0)
        
        # Calculate the FFT for each channel and add the values to fft_vals
        fft_vals[0] = np.abs(np.fft.fft(y1_vals))
        fft_vals[1] = np.abs(np.fft.fft(y2_vals))
        fft_vals[2] = np.abs(np.fft.fft(y3_vals))


    plt.clf()

    # Plot the time-domain signals

    plt.subplot(3, 1, 1)
    plt.plot(x_vals, y1_vals, label='Channel 1')
    plt.fill_between(x_vals, y1_vals, color='lightblue', alpha=0.4)
    plt.legend(loc='upper left')
    plt.title('Channel 1')
    plt.xlabel('Time')
    plt.ylabel('Measurement_1')
    plt.style.use('fivethirtyeight')

    plt.subplot(3, 1, 2)
    plt.plot(x_vals, y2_vals, label='Channel 2')
    plt.fill_between(x_vals, y2_vals, color='lightgreen', alpha=0.4)
    plt.legend(loc='upper left')
    plt.title('Channel 2')
    plt.xlabel('Time')
    plt.ylabel('Measurement_2')
    plt.style.use('bmh')

    plt.subplot(3, 1, 3)
    plt.plot(x_vals, y3_vals, label='Channel 3')
    plt.fill_between(x_vals, y3_vals, color='pink', alpha=0.4)
    plt.legend(loc='upper left')
    plt.title('Channel 3')
    plt.xlabel('Time')
    plt.ylabel('Measurement_3')
    plt.style.use('ggplot')

    # Plot the frequency-domain signals
    fig, axs = plt.subplots(3, 1, sharex=True)
    axs[0].plot(np.abs(fft_vals[0]), label='Channel 1')
    axs[0].legend(loc='upper left')
    axs[0].set_title('Channel 1 FFT')
    axs[1].plot(np.abs(fft_vals[1]), label='Channel 2')
    axs[1].legend(loc='upper left')
    axs[1].set_title('Channel 2 FFT')
    axs[2].plot(np.abs(fft_vals[2]), label='Channel 3')
    axs[2].legend(loc='upper left')
    axs[2].set_title('Channel 3 FFT')
    

    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=100)

plt.show()

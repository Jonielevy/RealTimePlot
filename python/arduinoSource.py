import serial
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with the port your Arduino is connected to
ser.flushInput()

x_vals = []
y1_vals = []
y2_vals = []
y3_vals = []

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

    plt.clf()

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

    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=100)

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Import data using Pandas (install with: pip install pandas)
data = pd.read_csv("data.csv")
print(data)

# Retrieve data columns
D = data.to_numpy()
t = D[:,0]
pan = D[:,1]
tilt = D[:,2]
r_us = D[:,3] + 7 # to account for the sensor offset
r_tof = D[:,4] + 7

# Create a basic plot
plt.plot(t,r_us)
plt.plot(t,r_tof)
plt.legend(["us","tof"])
plt.ylabel("Range (mm)")
plt.xlabel("Time (s)")
plt.xlim([min(t),max(t)])
plt.savefig('basic.png') # Save plot to a file
plt.show()

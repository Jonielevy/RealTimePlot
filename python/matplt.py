import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)


x = np.arange(0, 2*np.pi, 0.01)
line1, = axs[0].plot(x, np.sin(x))
line2, = axs[1].plot(x, np.cos(x))
line3, = axs[2].plot(x, np.sin(x))

def animate(i):
    line1.set_ydata(np.sin(x + i / 50))
    line2.set_ydata(np.cos(x + i / 50))
    line3.set_ydata(np.sin(x + i / 50))  # update the data.
    return line1, line2, line3


ani = animation.FuncAnimation(
    fig, animate, interval=20, blit=True, save_count=50)




# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()
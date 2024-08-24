import matplotlib.pyplot as plt
import numpy as np


def mouse_move(event):
    x, y = event.xdata, event.ydata
    update_plot(x, y)


def update_plot(U, V):
    quiver.set_UVC(-X + U, -Y + V)
    plt.draw()


plt.style.use('_mpl-gallery-nogrid')
x = np.linspace(-4, 4, 10)
y = np.linspace(-4, 4, 10)
X, Y = np.meshgrid(x, y)

U = 1
V = 1

fig, ax = plt.subplots()
quiver = ax.quiver(X, Y, U, V, color="lightcoral", angles='xy',
                   scale_units='xy', scale=5, width=.005)
ax.set(xlim=(-5, 5), ylim=(-5, 5))
ax.format_coord = lambda x, y: ""

plt.connect('motion_notify_event', mouse_move)
plt.show()

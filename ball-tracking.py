import matplotlib.pyplot as plt
import numpy as np


def ball_move(rate):
    ball_coords[0] += rate
    update_plot(ball_coords)


def update_plot(UV):
    U, V = UV
    quiver.set_UVC(-X + U, -Y + V)
    plt.draw()


SIZE = 20
plt.style.use('_mpl-gallery-nogrid')
x = np.linspace(-SIZE, SIZE, 10)
y = np.linspace(-SIZE, SIZE, 10)
X, Y = np.meshgrid(x, y)

ball_coords = [-SIZE, 0]

fig, ax = plt.subplots(1, 1, figsize=(5, 5))
quiver = ax.quiver(X, Y, ball_coords[0], ball_coords[1], color="lightcoral",
                   angles='xy', scale_units='xy', scale=5, width=.005)
ax.set(xlim=(-(SIZE+1), SIZE+1), ylim=(-(SIZE+1), SIZE+1))
ax.format_coord = lambda x, y: ""

ball = plt.Circle(ball_coords, 0.3, color='cornflowerblue')
ax.add_patch(ball)
plt.axis('off')

rate = 0.1
for i in np.arange(0, SIZE*2, rate):
    ball_move(rate)
    plt.pause(0.01)

plt.show()

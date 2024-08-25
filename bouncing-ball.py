import matplotlib.pyplot as plt
import numpy as np
x = 2.5
y = 3
ball_coords = [x, y]
fig, ax = plt.subplots()

canvas = ax.scatter(x, y)
ax.set(xlim=(0, 5), ylim=(0, 5))

def ball_move(y_pos):
    ball_coords[1] = y_pos
    update_plot(ball_coords)

def update_plot(ball_coords):
    canvas.set_offsets(ball_coords)
    plt.draw()

rate = -0.06
path_down = np.arange(y, 0.1, rate)
damping_rate = 2

while True:
    for i in path_down:
        ball_move(i)
        plt.pause(0.01)
    path_up = path_down[::-1][:-damping_rate]
    for i in path_up:
        ball_move(i)
        plt.pause(0.01)
    path_down = path_up[::-1]
    if len(path_down)==0:
        break
plt.show()
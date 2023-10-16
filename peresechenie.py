import matplotlib.pyplot as plt
import numpy as np


def plot_intersection(func1, func2):
    x = np.linspace(-10, 10, 1000)
    y1 = eval(func1)
    y2 = eval(func2)
    fig, ax = plt.subplots()
    ax.plot(x, y1, label='y1')
    ax.plot(x, y2, label='y2')
    ax.set_title(f"Пересечение [{func2}] и [{func1}]")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid()
    idx = np.argwhere(np.diff(np.sign(y1 - y2)) != 0).reshape(-1) + 0
    x_intersect = x[idx]
    y_intersect = y1[idx]
    ax.plot(x_intersect, y_intersect, 'ro', label='Точка пересечения')
    ax.legend()
    plt.show()


plot_intersection('x', '-x + 5')

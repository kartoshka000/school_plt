import matplotlib.pyplot as plt
import numpy as np

def create_subplot(ax, func, title):
    x = np.linspace(-10, 10, 500)
    y = func(x)
    ax.plot(x, y)
    ax.set_title(title)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

create_subplot(axs[0, 0], np.cos, 'График функции y = cos(x)')
create_subplot(axs[0, 1], np.sin, 'График функции y = sin(x)')
create_subplot(axs[1, 0], lambda x: x**2, 'График функции y = x^2')
create_subplot(axs[1, 1], lambda x: 2/x, 'График функции y = 2/x')

plt.suptitle('Графики функций', fontsize=16)
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

def stolb():
    data = np.random.randint(0, 100, size=7)
    x_labels = ['1', '2', '3', '4', '5', '6', '7']
    fig, ax = plt.subplots()
    ax.bar(x_labels, data)
    ax.set_title('Рандомный столбчатый график')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)
    plt.show()

stolb()
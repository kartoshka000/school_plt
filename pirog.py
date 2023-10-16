import random
import matplotlib.pyplot as plt


def pie_chart(n):
    data = [random.randint(1, 100) for i in range(n)]
    plt.title("Пирожок")
    labels = [f"Подпись {i}" for i in range(1, n + 1)]
    plt.pie(data, labels=labels, autopct='%1.1f%%')
    plt.show()


pie_chart(5)

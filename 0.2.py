import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x ** 2


def g(x):
    return 1 / x


def h(x):
    return x * np.sin(x)


x = np.arange(0.1, 5, 0.1)

fig, axes = plt.subplots(figsize=(13, 8))
axes.plot(x, f(x), label='$x^2$')
axes.plot(x, g(x), label='$\\frac{1}{x}$')
axes.plot(x, h(x), label=r'$x \cdot sin(x)$')
# axes.legend(['f(x)', 'g(x)', 'h(x)'])
axes.set_xlabel('x', fontsize=18)
axes.set_title('Title', fontsize=30)
axes.legend(loc=5, fontsize=18)
plt.show()

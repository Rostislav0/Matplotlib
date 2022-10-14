import matplotlib.pyplot as plt
import numpy as np


def f(x, a, b):
    x = np.delete(x, np.where(x == 0))
    return (x ** b + a ** b) / x ** b


x = np.arange(-40, 40, dtype=float)
fig, axes = plt.subplots(figsize=(13, 8))

axes.plot(f(x, 1, 2), color='red', linewidth=0, marker='*', markersize=15, markeredgewidth=2, markerfacecolor='white', label='\u03B1 = 1, \u03B2 = 1')
axes.plot(f(x, 1, 1), 'b', linestyle=':', alpha=0.1, lw=5, label='\u03B1 = 2, \u03B2 = 1')
axes.plot(f(x, 2, 1), 'g', lw=2, ls='-.', label='\u03B1 = 1, \u03B2 = 2')


axes.legend()
plt.show()

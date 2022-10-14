import matplotlib.pyplot as plt
import numpy as np

x = range(-10, 10)
y = [i ** 2 for i in x]

# plt.figure(figsize=(13, 8), dpi=120)
# plt.plot(x, y, 'r')
# plt.plot(y, x)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Title')
# plt.show()
# # plt.savefig('1.png')

# fig = plt.figure()
# axes = fig.add_axes([0, 0, 1, 1])
# axes.plot(x, y, 'r')
# axes2 = fig.add_axes([0.3, 0.5, 0.4, 0.4])
# axes2.plot(y, x, 'g')
# plt.show()

fig, axes = plt.subplots(2, 2, figsize=(12, 6))
axes[0][0].plot(x, y, 'r')
axes[0][0].set_title('First')
axes[0][0].set_xlabel('X_1')

axes[0][1].plot(y, x, 'g')
axes[0][1].set_title('Second')
axes[0][1].set_xlabel('X_2')

axes[1][0].plot(x, x, 'r')
axes[1][0].set_title('First')
axes[1][0].set_xlabel('X_1')

axes[1][1].plot(y, y, 'g')
axes[1][1].set_title('Second')
axes[1][1].set_xlabel('X_2')

fig.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0, 10, 11)
b = a ** 4

x = np.arange(0, 10)
y = 2 * x

fig, axes = plt.subplots(nrows=2, ncols=2)
axes[0][0].plot(x, y)
axes[0][1].plot(a, b)
plt.tight_layout()
fig.subplots_adjust(wspace=0.9)
plt.show()
print(type(axes))
# all title , limits , same as before

# subtitle for whole figure title
# saving is also same

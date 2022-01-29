import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 11, 10)
fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

ax.plot(x, x ** 2, label="x**2")
ax.plot(x, x ** 3, label="x**3")
ax.legend(loc=4)

# loc parameter , is where u want to see it : all one google search


# adding legend

plt.show()

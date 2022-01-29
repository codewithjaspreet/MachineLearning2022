import numpy as np
import matplotlib.pyplot as plt

# Data
a = np.linspace(0, 10, 11)
b = a ** 4
x = np.arange(0, 10)
y = 2 * x
fig = plt.figure()

# large axes

axes1 = fig.add_axes([0, 0, 1, 1])
axes1.plot(a, b)
axes1.set_xlim(0, 8)
axes1.set_ylim(0, 8000)
axes1.set_xlabel('A')
axes1.set_ylabel('B')
axes1.set_title('power of 4')
print(type(axes1))
axes2 = fig.add_axes([0.2, 0.2, 0.5, 0.5])
axes2.plot(a, b)
axes2.set_xlim(1, 2)
axes2.set_ylim(0, 50)
axes2.set_xlabel('A')
axes2.set_ylabel('B')
axes2.set_title('Zoomed in')

plt.show()
fig.savefig('C:\\Users\\kulveer singh sodhi\\Desktop\\new.png', bbox_inches='tight')
# fig-size & dpi can be used to make fdiff size figures'
# fig.savefig  again will save the figures as basic
# bbox_inches saves x and y-axis too in image

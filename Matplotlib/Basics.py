import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10)
y = 2 * x
plt.plot(x, y)
plt.title('String Title')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.xlim(0, 6)
plt.ylim(0, 15)
plt.savefig('C:\\Users\\kulveer singh sodhi\\Desktop\\myfirstplot.png')
plt.show()
# add title

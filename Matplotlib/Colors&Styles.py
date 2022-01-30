import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 11, 10)

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])

ax.plot(x, x, color='blue', lw=2, ls='--', marker='o', ms=20)

# marker , marker-size , marker-edge-width , marker-edge-color
# any hex color code is allowed
# lw
# # custom line style is also available
# lines = ax.plot(x, x + 1, color='purple', lw=5)
# lines[0].set_dashes([1, 2, 1, 2, 10, 2])
# line-styles


plt.show()
# colors

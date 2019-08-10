import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 50)
y = np.sin(x)

plt.plot(x, y, 'ro-.')
plt.plot(x, 2 * y, 'g.-')

plt.show()
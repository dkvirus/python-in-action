import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 50)
y = np.sin(x)

plt.plot(x, y, label='y=sin(x)')
plt.plot(x, 2 * y, label='y=2sin(x)')
plt.legend()   

plt.title("Matplotlib")  

plt.show()
import matplotlib.pyplot as plt
import numpy as np

# 绘制 y = sin(x) 函数的曲线
x = np.linspace(0, 2 * np.pi, 50)
y = np.sin(x)

plt.plot(x, y)
plt.show()


import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2*np.pi, 0.1)   # start,stop,step
y = np.sin(x)
z = np.cos(x)
tan = np.tan(x)

plt.plot(x, y, x, z)
plt.ylim(-1, 1)
plt.plot(x, tan)
plt.legend(labels=["sin", "cos", "tan"], loc="lower left")
lt.show()



def project1():
    import matplotlib.pyplot as plt
    import numpy as np

    x = np.arange(0, 2*np.pi, 0.1)
    y = np.sin(x)
    z = np.cos(x)
    tan = np.tan(x)
    
    plt.plot(x, y, x, z, x, tan)
    plt.ylim(-1, 1)
    plt.legend(labels=["sin", "cos", "tan"], loc="lower left")
    plt.show()

if __name__ == "__main__":
    project1()
    



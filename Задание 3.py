import matplotlib.pyplot as plt
import numpy as np

def plot():
    x = np.linspace(-5,5,40)
    y = x
    z = np.sin((x**(y)))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z)
    plt.show()
if __name__ == '__main__':
    plot()

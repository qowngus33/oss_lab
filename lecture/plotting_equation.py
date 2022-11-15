import matplotlib.pyplot as plt

if __name__ == "__main__":
    scale = 10
    xs = [x/scale for x in range(-4*scale, 10*scale)]
    ys = [0.1*x**3 - 0.8*x**2 - 1.5*x + 5.4 for x in xs]

    plt.title('$y = 0.1x^3 - 0.8x^2 - 1.5x + 5.4$') # LaTeX style
    plt.plot(xs, ys, 'r-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.axis('equal')
    plt.show()

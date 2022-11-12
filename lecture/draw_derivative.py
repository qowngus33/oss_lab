import matplotlib.pyplot as plt


if __name__ == "__main__":
    scale = 10
    xs = [x/scale for x in range(-4*scale, 10*scale)]
    ys = [0.1*x**3 - 0.8*x**2 - 1.5*x + 5.4 for x in xs]
    yt = [-3.5*x + 7 for x in xs]

    plt.plot(xs, ys, 'r-', label='y')
    plt.plot(xs, yt, 'b--', label='tangent line at x=2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend()
    plt.show()

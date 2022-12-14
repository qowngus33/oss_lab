import numpy as np
import matplotlib.pyplot as plt

f = lambda x: 0.1*x**3 - 0.8*x**2 - 1.5*x + 5.4
fd = lambda x: 0.3*x**2 - 1.6*x - 1.5
fdd = lambda x: 0.6*x - 1.6

viz_range = np.array([-6, 12])
learn_rate = 0.1 # Try 0.001, 0.01, 0.5, and 0.6
max_iter = 100
min_tol = 1e-6
x_init = 12 # Try -2

if __name__ == "__main__":
    # Prepare visualization
    xs = np.linspace(*viz_range, 100)
    plt.plot(xs, f(xs), 'r-', label='f(x)', linewidth=2)
    plt.plot(x_init, f(x_init), 'b.', label='Each step', markersize=12)

    # 여러 개의 인자를 받기 위해서 *args 형태로 파라미터를 작성
    plt.axis([*viz_range, *f(viz_range)])
    plt.legend()

    x = x_init
    for i in range(max_iter):
        xp = x
        x = x - learn_rate * fd(x)  # => gradient descent
        # x = x - fd(x) / fdd(x) # => newton
        # x = x - f(x) / fd(x) => gauss-newton

        print(f'Iter: {i}, x = {xp:.3f} to {x:.3f}, f(x) = {f(xp):.3f} to {f(x):.3f} (f\'(x) = {fd(xp):.3f})')
        lcolor = np.random.rand(3)

        approx = fd(xp)*(xs-xp)+f(xp)  # => gradient descent
        # approx = 0.5 * fdd(xp) * (xs - xp) ** 2 + fd(xp) * (xs - xp) + f(xp)  # => newton

        plt.plot(xs, approx, '-', linewidth=1, color=lcolor, alpha=0.5)
        plt.plot(x, f(x), '.', color=lcolor, markersize=12)
        # Check the terminal condition
        if abs(x - xp) < min_tol:
            break

    plt.show()

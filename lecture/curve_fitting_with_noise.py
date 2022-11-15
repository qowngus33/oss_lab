import numpy as np
import matplotlib.pyplot as plt

def buildA(order, xs):
    A = np.empty((0, len(xs)))
    for i in range(order + 1):
        A = np.vstack((xs**i, A))
    return A.T

if __name__ == "__main__":
    true_coeff = [0.1, -0.8, -1.5, 5.4]
    poly_order = 3
    data_range = (-6, 12)
    data_num = 10
    noise_std = 0.5

    x = np.random.uniform(data_range[0],data_range[1],size=data_num)
    y = buildA(len(true_coeff) - 1, x) @ true_coeff

    xn = x + np.random.normal(scale=noise_std, size=x.shape)
    yn = y + np.random.normal(scale=noise_std, size=y.shape)

    A = buildA(poly_order, xn)
    b = yn
    coeff = np.linalg.pinv(A) @ b

    # Plot the data and result
    plt.title(f'Order: {poly_order}, Coeff: ' + np.array2string(coeff, precision=2, suppress_small=True))
    xc = np.linspace(*data_range, 100)

    # true line
    plt.plot(xc, np.matmul(buildA(len(true_coeff) - 1, xc), true_coeff), 'k-', label='The true curve', alpha=0.2)

    # noisy data
    plt.plot(xn, yn, 'b.', label='Noisy data')

    # estimate
    plt.plot(xc, np.matmul(buildA(poly_order, xc), coeff), 'g-', label='Estimate')

    plt.xlim(data_range)
    plt.legend()
    plt.show()

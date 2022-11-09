import numpy as np
import matplotlib.pyplot as plt

true_line = lambda x: -2/3*x + 14/3
data_range = np.array([-4,12])
data_num = 100
noise_std = 0.5

x = np.random.uniform(data_range[0],data_range[1],size=data_num)
y = true_line(x)

xn = x + np.random.normal(scale=noise_std, size=x.shape)
yn = y + np.random.normal(scale=noise_std, size=y.shape)

A = np.vstack((xn, np.ones(xn.shape))).T
b = yn
line = np.linalg.pinv(A) @ b

plt.title(f'Line: y={line[0]:.3f}*x + {line[1]:.3f}')

# "-": 실선, "--": 점선, ".": 점
plt.plot(data_range, true_line(data_range), '-r', label='The true line')
plt.plot(xn, yn, 'b.', label='Noisy data')
plt.plot(data_range, line[0]*data_range + line[1], 'g-', label='Estimate')

# X축이 표시되는 범위를 지정하거나 반환
plt.xlim(data_range)

# show legend(범례)
plt.legend()
plt.show()

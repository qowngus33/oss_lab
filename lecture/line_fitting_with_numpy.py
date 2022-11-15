import numpy as np
from scipy import linalg

if __name__ == "__main__":
    A = np.array([[1,4,1],[1,2,1]])
    x = linalg.null_space(A)
    print(x / x[0])

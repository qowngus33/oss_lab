import numpy as np

if __name__ == "__main__":
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print(A.ndim, A.size, A.shape, A.dtype)

    print(A + B)
    print(A - B)
    print(A * B)
    print(A @ B)
    print(A / B)

    print(A.T)
    # rank: maximal number of linearly independent columns of A
    print(np.linalg.matrix_rank(A)) # 2, full rank
    print(np.linalg.det(A))
    print(np.linalg.inv(A))
    print(np.linalg.pinv(A))
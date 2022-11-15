import numpy as np

if __name__ == "__main__":
    pts = np.array([(1,4),(4,2),(7,1)])

    # line fitting
    A = np.vstack((pts[:,0], np.ones(len(pts)))).T
    b = pts[:,1]

    x = np.matmul(np.linalg.pinv(A), b)
    print(x)
    print(np.round(x))


import numpy as np

if __name__ == "__main__":
    p = np.array([1/6,1/6,1/6,1/6,1/6,1/6])
    entropy = sum(-p*np.log2(p))
    print(entropy)

    q = np.array([0.4, 0.4, 0.05, 0.05, 0.05, 0.05])
    cross_entropy = sum(-p * np.log2(q))  # level of difference between two probability distributions
    print(cross_entropy)

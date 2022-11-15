import numpy as np

# vectors
a = np.array([1, 4, 1])
b = np.array([4, 2, 1])

if __name__ == "__main__":
    # dot product
    dot_product = a.dot(b)
    print(dot_product)

    cross_product = np.array(np.cross(a, b))
    print(cross_product)

    a_norm = np.linalg.norm(a)
    b_norm = np.linalg.norm(b)

    # dot product
    cos_theta = dot_product / (a_norm * b_norm)
    theta = np.arccos(cos_theta)
    print(f'cos({theta * 180 / np.pi}) = {cos_theta}')

    # cross product
    sin_theta = cross_product.dot(cross_product)**(1/2) / (a_norm * b_norm)
    theta = np.arcsin(sin_theta)
    print(f'sin({theta * 180 / np.pi}) = {sin_theta}')

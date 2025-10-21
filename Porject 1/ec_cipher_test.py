import math, numpy as np

def ec_formula(row):
    # paste your TuringBot-generated function here
    return 0.432357 + (-0.498752 * math.cos(
        0.594808 * (-4.10993 * math.cosh(row) -
        (0.590558 + math.atanh(math.cos(
        math.tan(math.cos(row/(-0.00153462))) + row*row))))))

def ec_cipher(N, key):
    arr = np.empty(N)
    arr[0] = key
    for i in range(N-1):
        arr[i+1] = ec_formula(arr[i])
    return arr

print(ec_cipher(10, 0.5))

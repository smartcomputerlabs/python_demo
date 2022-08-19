import numpy as np

A = np.array([[10, 3, 5],
              [7, 9, 2],
              [11, 6, 9]], dtype=int)
a = np.zeros((3,6))
for i in range(len(a)):
    for j in range(len(a[i])):
        a [i][j] = np.random.randint(100)
print (a)

# Find transpose
a_t = np.zeros((6,3))
for i in range(len(a)):
    # Iterate through columns
    for j in range(len(a[i])):
        a_t[j][i] = a[i][j]
print (a_t)
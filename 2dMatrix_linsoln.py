import numpy as np

A = np.array([[np.random.randint(101),np.random.randint(101),np.random.randint(101)],
              [np.random.randint(101),np.random.randint(101),np.random.randint(101)],
              [np.random.randint(101),np.random.randint(101),np.random.randint(101)]], dtype=int)

B = np.array([[np.random.randint(101)],
              [np.random.randint(101)],
              [np.random.randint(101)]],dtype=int)
for i in range(len(B)):
    for j in range(len(B[i])):
        B [i][j] = np.random.randint(101)

X = np.linalg.solve(A,B)
print (X)
print (np.allclose(np.dot(A, X), B))
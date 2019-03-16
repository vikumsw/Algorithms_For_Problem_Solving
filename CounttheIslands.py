'''
Challenge Count the Islands:
This problem was asked by Amazon.

Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
'''

import numpy as np

def calc_islands(A):
    count = 0;
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j]==1:
                #print(np.matrix(A))
                count += 1
                mark_island(A,i,j,count)
    return count
    
    
def mark_island(A,i,j,count):
    if A[i][j]==1:
        A[i][j] = count*10
        for k in range(-1, 2):
            for l in range(-1, 2): 
                mark_island(A,i+k,j+l,count)

A = [
        [1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1],
        [1, 1, 0, 0, 1]
    ]
A = np.pad(A, pad_width=1, mode='constant', constant_values=-1)
print("Island Count :",calc_islands(A))
print(np.matrix(A))
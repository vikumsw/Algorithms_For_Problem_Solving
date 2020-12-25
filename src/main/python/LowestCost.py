'''
This problem was asked by Facebook.
A builder is looking to build a row of N houses that can be of K different colors.
He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color,
return the minimum cost which achieves this goal.
'''

'''
       K
  0   1 2 3
N 1   5 1 4
  2   6 7 1
'''

#mat = [[1,2,3],[5,1,4],[6,7,1]]
mat = [[1,7,1,4],[9,1,3,6],[6,2,3,5],[3,5,1,9]]
K,N = len(mat[0]), len(mat)
cost =0
for i in range(N):
    cost += cost + sum(mat[i])
print('Initial Min Cost:', cost)

def minCost(currentCost,n,k):
    global cost
    currentCost += mat[n][k]
    if (n==N-1):
         cost = currentCost if (currentCost < cost) else cost
    else:
        for i in range(K):
            if i==k:
                continue
            minCost(int(currentCost),n+1,i)

for i in range(K):
    minCost(0,0,i)

print('Min Cost = ', cost)
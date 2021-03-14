class Solution:
    def rotate90Clockwise(self,A):
        N = len(A[0])
        for i in range(N // 2):
            for j in range(i, N - i - 1):
                temp = A[i][j]
                A[i][j] = A[N - 1 - j][i]
                A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
                A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
                A[j][N - 1 - i] = temp
                
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        self.rotate90Clockwise(mat)
        
        for i in range(4):
            if mat==target: return True
            self.rotate90Clockwise(mat)
            
        return False
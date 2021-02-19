'''
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
'''
def MatRotate(mat):
    row_count = len(mat)
    if row_count==0:return
    col_count = len(mat[0])
    replaced = set()

    def replace(r,c,val):
        mat[r][c]=val
        replaced.add((r,c))

    for r in range(row_count):
        for c in range(col_count):
            if (r,c) in replaced: continue

            t1 = mat[r][c]
            t2 = mat[c][row_count-1-r]
            t3 = mat[row_count-1-r][row_count-1-c]
            t4 = mat[row_count-1-c][r]

            replace(c,row_count-1-r,t1)
            replace(row_count-1-r,row_count-1-c,t2)
            replace(row_count-1-c,r,t3)
            replace(r,c,t4)

def PrintMat(mat):
    print('-'*30)
    for r in mat:
        print(r)

if __name__=='__main__':
    mat = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    PrintMat(mat)
    MatRotate(mat)
    PrintMat(mat)

    mat = [
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9']
    ]
    PrintMat(mat)
    MatRotate(mat)
    PrintMat(mat)


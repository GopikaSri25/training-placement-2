class Solution(object):
    def areSimilar(self, mat, k):
        m=len(mat)
        n=len(mat[0])
        matrix=[]
        for i in range(m):
            row=[]
            for j in range(n):
                row.append(mat[i][j])
            matrix.append(row)
        for x in range(k%n):
            for i in range(m):
                if(i%2==0):
                    key=mat[i][0]
                    j=0
                    while j<n-1:
                        mat[i][j]=mat[i][j+1]
                        j+=1
                    mat[i][n-1]=key
                else:
                    key=mat[i][n-1]
                    j=n-1
                    while j>0:
                        mat[i][j]=mat[i][j-1]
                        j-=1
                    mat[i][0]=key
        for i in range(m):
            for j in range(n):
                if matrix[i][j]!=mat[i][j]:
                    return False
        return True

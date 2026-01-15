class Solution(object):
    def constructArray(self, n, k):
        p=[i for i in range(1,n+1)]
        res=[]
        i=0
        j=n-1
        f=1
        while k!=0:
            if k==1:
                if f==1:
                    for i in range(j,i-1,-1):
                        res.append(p[i])
                else:
                    for i in range(i,j+1):
                        res.append(p[i])
                k=k-1
            else:
                if f==1:
                    f=0
                    res.append(p[j])
                    j=j-1
                else:
                    f=1
                    res.append(p[i])
                    i=i+1
                k=k-1
        return res

        

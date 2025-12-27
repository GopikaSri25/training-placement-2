class Solution(object):
    def alternateDigitSum(self, n):
        res=0
        n=str(n)
        for i in range(len(n)):
            if i%2==0:
                res+=int(n[i])
            else:
                res-=int(n[i])
        return res

            
            


            



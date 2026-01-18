class Solution(object):
    def rotatedDigits(self, n):
        x=0
        for i in range(2,n+1):
            a=0
            s=""
            for j in str(i):
                if(j in "347"):
                    a+=1
                    break
                else:
                    if(j in "018"):
                        s=s+j
                    elif(j=="2"):
                        s=s+"5"
                    elif(j=="5"):
                        s=s+"2"
                    elif(j=="6"):
                        s=s+"9"
                    elif(j=="9"):
                        s=s+"6"
            if(a==0 and i!=int(s)):
                print(i)
                x+=1
        return x

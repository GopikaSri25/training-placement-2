class Solution(object):
    def isBalanced(self, num):
        a=0
        b=0
        for i in range(len(num)):
            if int(i)%2==0:
                a+=int(num[i])
            else:
                b+=int(num[i])
        if a==b:
            return True
        return False
        

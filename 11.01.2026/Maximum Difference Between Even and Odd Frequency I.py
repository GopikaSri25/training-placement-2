class Solution(object):
    def maxDifference(self, s):
        p=""
        odd=-999999
        even=999999
        for i in s:
            if i not in p:
                p=p+i
        for i in p:
            c=s.count(i)
            if(c%2!=0):
                odd= max(odd,c)
            else:
                even = min(even,c)
        return odd-even if odd != -999999 and even != 999999 else 0

        

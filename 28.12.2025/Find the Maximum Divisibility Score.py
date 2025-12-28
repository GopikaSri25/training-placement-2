class Solution(object):
    def maxDivScore(self, nums, s):
        l=[]
        a=0
        o=max(s)
        for x in s:
            for y in nums:
                if y%x==0:
                    a=a+1
            l.append(a)        
            a=0
        a=max(l)
        for x in range(len(l)):
            if l[x]==a and s[x]<o:
                o=s[x]
        return o
                    

        

class Solution(object):
    def minDeletion(self, s, k):
        a=""
        l=[]
        for x in s:
            if x not in a:
                a=a+x
                l.append(s.count(x))
        l.sort()
        if len(set(s))-k<=0:
            return 0
        else:
            return sum(l[:len(set(s))-k])
        

class Solution(object):
    def findPermutationDifference(self, s, t):
        c=0
        def fi(a):
            for i in range(len(t)):
                if t[i]==a:
                    return i

        for i in range(len(s)):
            c+=abs(i-fi(s[i]))
        return c
        

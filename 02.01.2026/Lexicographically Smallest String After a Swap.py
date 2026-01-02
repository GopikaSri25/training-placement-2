class Solution(object):
    def getSmallestString(self, s): 
        n = len(s)

        for i in range(n-1):
            if int(s[i]) % 2 == int(s[i+1]) % 2 and s[i] > s[i+1]:
                s = s[:i] + s[i+1] + s[i] + s[i+2:]
                break
        return s

class Solution(object):
    def findValidPair(self, s):
        for i in range(len(s)-1):
            x=""
            if s.count(s[i])==int(s[i]) and s.count(s[i+1])==int(s[i+1]) and s[i]!=s[i+1]:
                x+=s[i]
                x+=s[i+1]
                break
        return x
        

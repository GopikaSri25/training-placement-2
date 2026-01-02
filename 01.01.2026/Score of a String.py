class Solution(object):
    def scoreOfString(self, s):
        su=0
        for i in range(1,len(s)):
            su+=abs(ord(s[i])-ord(s[i-1]))
        return su
        

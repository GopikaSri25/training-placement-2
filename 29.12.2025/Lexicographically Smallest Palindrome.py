class Solution(object):
    def makeSmallestPalindrome(self, s):
        s = list(s)
        start = 0
        end = len(s) - 1
        while start<=end:
            if s[start]<s[end]:
                s[end]=s[start]
            elif s[start]>s[end]:
                s[start]=s[end]
            start+=1
            end-=1
        
        return "".join(s)

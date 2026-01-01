class Solution(object):
    def isSubstringPresent(self, s):
        
        substringFound = False

        for i in range(len(s)-1):
            forwardSubstring = [s[i],s[i+1]]
            for j in range(1,len(s)):
                if forwardSubstring[0] == s[j] and forwardSubstring[1] == s[j-1]:
                    substringFound = True
                    break
        
        return(substringFound)
        

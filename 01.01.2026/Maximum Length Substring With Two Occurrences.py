class Solution(object):
    def maximumLengthSubstring(self, s):
        d={}
        p=""
        left=0
        max1=0

        for right in range(len(s)):
            x=s[right]
            d[x]=d.get(x,0)+1

            if d[x]>2:
                while(d[x]>2):
                    d[s[left]]=d.get(s[left],0)-1
                    left+=1
            len1=right-left+1
            max1=max( len1,max1)
        return max1
                
                    

        

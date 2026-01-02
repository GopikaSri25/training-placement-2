class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        ret = 0 
        n=len(colors)
        for i in range(n):
            if colors[i%n]!=colors[(i-1)%n] and colors[i%n]!=colors[(i+1)%n]:
                ret+=1
        return ret

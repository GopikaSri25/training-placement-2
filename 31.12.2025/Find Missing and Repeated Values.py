class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        res = []
        temp = []
        for i in grid:
            temp += i
        
        temp1 = []
        for i in temp:
            if i not in temp1:
                temp1.append(i)
            else:
                res.append(i)
                break
        
        for i in range(1,len(temp)+1):
            if i not in temp:
                res.append(i)
        
        return res
        

        

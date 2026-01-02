class Solution(object):
    def minElement(self, nums):
        res = []
        for i in nums:
            s = str(i)
            temp = 0
            for j in s:
                temp += int(j)
            res.append(temp)
        return min(res)

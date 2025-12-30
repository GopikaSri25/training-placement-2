class Solution(object):
    def minOperations(self, nums, k):
        count = 0
        need = set()
        for i in range(1, k + 1):
            need.add(i)
        while (len(nums) != 0):
            x = nums.pop()
            count += 1
            if x in need:
                need.remove(x)
            if (len(need) == 0):
                break
        return count

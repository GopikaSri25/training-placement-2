class Solution(object):
    def minNumber(self, nums1, nums2):
        sim = []
        for i in nums1:
            if i in nums2:
                sim.append(i)
        if sim != []:
            return min(sim)
        min1 = min(nums1)
        min2 = min(nums2)
        if min1 > min2:
            return 10*min2 + min1
        return 10*min1 + min2

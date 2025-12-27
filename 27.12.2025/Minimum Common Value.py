class Solution(object):
    def getCommon(self, nums1, nums2):
        set1= set(nums1)
        set2= set(nums2)
        new = list(set1&set2)
        if len(new)>0:
            return min(new)
        else:
            return -1

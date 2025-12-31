class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        c1= 0
        c2= 0
        for i in list(set(nums1) & set(nums2)):
            c1 += nums1.count(i)
            c2 += nums2.count(i)
        return [c1,c2]



        

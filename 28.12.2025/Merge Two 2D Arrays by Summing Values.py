class Solution(object):
    def mergeArrays(self, nums1, nums2):
        nums3 = [0] * 1001
        for i in nums1:
            nums3[i[0]] += i[1]
        for j in nums2:
            nums3[j[0]] += j[1]
        ret = []
        index = 0
        for k in nums3:
            if k > 0:
                ret.append([index,k])
            index += 1
        return ret

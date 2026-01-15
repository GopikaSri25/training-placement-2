class Solution(object):
    def isPossible(self, nums):
        n, listEnd, listSize  = len(nums), [], []
        if n < 3:
            return False
        listEnd.append(nums[0])
        listSize.append(1)
        for i in range(1, n):
            num = nums[i]
            correctListIndex = self.getCorrectListIndex(listEnd, listSize, num-1)
            if correctListIndex == -1:
                listEnd.append(num)
                listSize.append(1)
            else:
                listEnd[correctListIndex] = num
                listSize[correctListIndex] += 1

        for i in range(len(listSize)):
            if listSize[i] < 3:
                return False
        
        return True

    def getCorrectListIndex(self, listEnd, listSize, num):
        retIndex, sizeVal = -1, float('inf')
        for i in range(len(listEnd)):
            if listEnd[i] == num and listSize[i] < sizeVal:
                retIndex = i
                sizeVal = listSize[i]
        return retIndex

        

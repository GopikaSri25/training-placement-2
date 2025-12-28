class Solution(object):
    def distinctDifferenceArray(self, nums):
        leftMap = {nums[0]: 1}
        rightMap = {}
        for num in nums[1:]:
            rightMap[num] = rightMap.get(num, 0) + 1

        results = []

        for i, value in enumerate(nums):
            if i > 0:
                leftMap[value] = 1

                if value in rightMap and rightMap[value] > 0:
                    rightMap[value] -= 1
                if value in rightMap and rightMap[value] == 0:
                    rightMap.pop(value)

            results.append(len(leftMap) - len(rightMap))

        return results

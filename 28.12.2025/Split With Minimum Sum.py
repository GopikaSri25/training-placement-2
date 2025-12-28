class Solution(object):
    def splitNum(self, num):
        sortedString = ''.join(sorted(str(num)))
        num1 = ""
        num2 = ""
        for i in range(len(sortedString)):
            if i%2 == 0:
                num1 += sortedString[i]
            else:
                num2 += sortedString[i]
        return int(num1)+int(num2)

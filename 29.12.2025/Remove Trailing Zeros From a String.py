class Solution(object):
    def removeTrailingZeros(self, num):
        if '0' not in num:
            return num
        num1=num[::-1]
        for i in range(0,len(num)):
            if num1[i] !='0':
                num1= num1[i:]
                print(num1)
                break
        return num1[::-1]

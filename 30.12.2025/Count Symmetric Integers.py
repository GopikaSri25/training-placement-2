class Solution(object):
    def countSymmetricIntegers(self, low, high):
        count=0
        for i in range((low),(high)+1):
            s=str(i)
            if len(s)%2==0:
                half = len(s) // 2
                left_sum = sum(int(x) for x in s[:half])
                right_sum = sum(int(x) for x in s[half:])
                if left_sum == right_sum:
                    count += 1
        return count

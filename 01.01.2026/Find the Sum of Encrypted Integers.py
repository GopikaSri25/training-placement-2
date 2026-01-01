class Solution(object):
    def sumOfEncryptedInt(self, nums):
        sum=0
        for num in nums:
            if num>9:
                count=max=0
                while num>0:
                    d=num%10
                    if d>max:
                        max=d
                    count+=1
                    num//=10
                num=0
                for i in range(count):
                    num=num*10+max
                sum+=num
            else:
                sum+=num
        return sum

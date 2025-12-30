class Solution(object):
    def differenceOfSums(self, n, m):
        range_sum=n*(n+1)/2
        num2=0
        i=1
        while(i*m<=n):
            num2+=i*m
            i+=1
        return (range_sum-num2)-num2

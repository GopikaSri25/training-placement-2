class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        sum=0
        if k>numOnes:
            sum+=numOnes
            k-=numOnes
        else:
            sum+=k
            k=0
        if k>numZeros:
            k-=numZeros
        else:
            k=0
        if k>numNegOnes:
            sum-=numNegOnes
            k-=numNegOnes
        else:
            sum-=k
        return sum
      

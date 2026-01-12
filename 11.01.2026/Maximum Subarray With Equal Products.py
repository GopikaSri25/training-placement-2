class Solution(object):
    def maxLength(self, nums):
        def gcd(a,b):
            while b:
                a,b = b,a%b
            return a
            
        def lcm(a,b):
            return abs(a*b) // gcd(a,b)
        n = len(nums)
        
        ml = 0
        for i in range(n):
            cg = nums[i]
            cl = nums[i]
            cp = nums[i]
            for j in range(i,n):
                if i != j:
                    cg = gcd(cg,nums[j])
                    cl = lcm(cl,nums[j])
                    cp *= nums[j]
                if cp == cg * cl:
                    ml = max(ml,j-i+1)
        return ml
                

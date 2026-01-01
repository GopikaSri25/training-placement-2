class Solution(object):
    def minimumSubarrayLength(self, nums, k):
        
        maxi = max(nums)

        if k == 0:
            return 1
        
        num_of_bits = 0
        
        cur = maxi

        while cur > 0:
            num_of_bits += 1
            cur >>= 1
        
        bit_arr = [0]*num_of_bits

        l = 0
        or_so_far = 0
        res = len(nums) + 1
        for r in range(len(nums)):
            or_so_far |= nums[r]

            cur = nums[r]
            j = 0
            while cur > 0:
                if cur & 1:
                    bit_arr[j] += 1
                j += 1
                cur >>= 1
            
            while or_so_far >= k:
                res = min(res, r-l+1)
                cur = nums[l]

                subtract_mask = 1
                j = 0
                while cur > 0:
                    if cur & 1:
                        bit_arr[j] -= 1
                        if bit_arr[j] == 0:
                            or_so_far -= subtract_mask
                    
                    j += 1
                    cur >>= 1
                    subtract_mask <<= 1
                
                l += 1
        
        if res > len(nums):
            return -1
        
        return res


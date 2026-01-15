class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        if desiredTotal == 0:
            return True
        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False
        
        memo = {}

        def canIWinHelper(used_numbers, target):
            if used_numbers in memo:
                return memo[used_numbers]
            
            for i in range(1, maxChoosableInteger + 1):
                current_bit = 1 << i
                if (used_numbers & current_bit) == 0:  # Check if the number i is available
                    if target - i <= 0 or not canIWinHelper(used_numbers | current_bit, target - i):
                        memo[used_numbers] = True
                        return True
            
            memo[used_numbers] = False
            return False

        return canIWinHelper(0, desiredTotal)

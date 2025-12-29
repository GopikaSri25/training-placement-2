class Solution(object):
    def buyChoco(self, prices, money):
        cur_m = money

        prices = sorted(prices)[::-1]
        for i in range(0 , 2):
            cur_smallest = prices.pop()
            if cur_smallest > cur_m:
                return money
            else:
                cur_m -= cur_smallest
        
        return cur_m

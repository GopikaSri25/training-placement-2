class Solution(object):
    def maxProfit(self, prices, fee):
        if not prices:
            return 0

        cash = 0
        hold = -prices[0]


        for price in prices[1:]:
            new_cash = max(cash, hold + price - fee)

            new_hold = max(hold, cash - price)


            cash, hold = new_cash, new_hold

        return cash
        

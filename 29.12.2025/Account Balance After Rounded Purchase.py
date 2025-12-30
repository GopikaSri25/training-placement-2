class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        i=0
        j=10
        if purchaseAmount%10==0:
            return 100-purchaseAmount
        while True:
            if i<purchaseAmount and purchaseAmount<j:
                if purchaseAmount-i<j-purchaseAmount:
                    return 100-i
                return 100-j
            i+=10
            j+=10

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyingprices = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            sellingprices = prices[i]
            if sellingprices > buyingprices:
                profit = max(profit, (sellingprices - buyingprices))
            if buyingprices > sellingprices:
                buyingprices = prices[i]
        return profit
           
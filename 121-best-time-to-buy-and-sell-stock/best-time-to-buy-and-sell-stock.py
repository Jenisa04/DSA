class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        sellsub = 0
        for stock in prices:
            if stock < lowest:
                lowest = stock
            sellsub =max(sellsub, stock-lowest)
        return sellsub
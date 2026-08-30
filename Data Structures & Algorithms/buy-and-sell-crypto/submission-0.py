class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minVal = 1000000
        maxVal = 0

        for price in prices:
            profit = price - minVal
            if price < minVal:
                minVal = price
            if profit > maxVal:
                maxVal = profit
        
        return maxVal
            
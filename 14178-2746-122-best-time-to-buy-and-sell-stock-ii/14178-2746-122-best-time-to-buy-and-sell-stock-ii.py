class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        max_prof = 0
        min_stock = prices[0]
        for i in prices:
            min_stock  = min(i, min_stock )

            if (i-min_stock) > 0:
                max_prof = max_prof+ i-min_stock
                min_stock = i
        return max_prof
        
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        max_prof = float('-inf')
        min_stock = prices[0]

        for i in prices:
            max_prof = max(max_prof, i -min_stock)
            min_stock = min(i,min_stock)
        return max_prof
        
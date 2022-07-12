from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0

        while r < len(prices) - 1:
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
                r += 1

        return max_profit


# test
prices = [7, 1, 5, 3, 6, 4]  # 5
prices_1 = [7, 6, 4, 3, 1]  # 0

Ex = Solution()
print(Ex.maxProfit(prices_1))
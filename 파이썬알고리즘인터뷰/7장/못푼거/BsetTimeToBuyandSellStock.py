import sys


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profile = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price,price)
            profile = max(profile, price- min_price)

        return profile


sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))

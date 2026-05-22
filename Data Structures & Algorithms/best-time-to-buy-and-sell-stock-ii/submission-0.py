class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n

        for i in range(1, n):
            if prices[i-1] < prices[i]:
                print(1, dp[i])
                dp[i] = prices[i] - prices[i-1]
                print(2, dp[i])

        print(dp)

        return sum(dp)

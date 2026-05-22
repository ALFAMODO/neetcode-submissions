class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        n = len(prices)
        dp = [0] * n

        for i in range(1, n):
            if prices[i-1] < prices[i]:
                dp[i] = prices[i] - prices[i-1]

        return sum(dp)
        '''

        price = 0

        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                price += prices[i] - prices[i-1]

        return price

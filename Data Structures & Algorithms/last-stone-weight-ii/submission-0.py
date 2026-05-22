class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        s = sum(stones)
        m = s//2

        dp = [[0] * (m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(0, m+1):
                pick = 0
                if stones[i-1] <= j:
                    pick = stones[i-1] + dp[i-1][j - stones[i-1]]
                
                notpick = dp[i-1][j]
                dp[i][j] = max(pick, notpick)

        return s - 2 * dp[n][m]
        
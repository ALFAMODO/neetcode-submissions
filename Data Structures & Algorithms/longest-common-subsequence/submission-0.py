class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int: 

        def bottom_up(m,n):
            dp = [[0] * (n+1) for _ in range(m+1)]

            for i in range(1, m+1):
                for j in range(1, n+1):
                    if text1[i-1] == text2[j-1]:
                        dp[i][j] =  1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

            return dp[m][n]  
        
        def top_down(m,n):
            memo= {}

            def dfs(i: int, j: int) -> int:
                if i == m or j == n:
                    return 0
                
                if (i,j) in memo:
                    return memo[(i, j)]
                
                if text1[i] == text2[j]:
                    res = 1 + dfs(i+1, j+1)
                else:
                    res = max(dfs(i+1,j), dfs(i, j+1))
            
                memo[(i, j)] = res
                return res
            
            return dfs(0, 0)
            
        m = len(text1)
        n = len(text2)
        res = top_down(m,n)

        return res   
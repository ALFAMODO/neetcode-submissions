class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def bottom_up(nums):
            dp = [1] * len(nums)

            for i in range(1, len(nums)):
                for j in range(i):
                    if nums[i] > nums[j]:
                        dp[i] = max(dp[i], dp[j] + 1)
            
            return max(dp)

        def top_down(nums):
            n=len(nums)
            memo = {}
            res=0
            def dfs(i):
                if i in memo:
                    return memo[i]
                
                temp = 1
                for j in range(i+1, n):
                    if nums[j] > nums[i]:
                        temp = max(temp, dfs(j)+1)
                    
                memo[i] = temp
                return temp
            
            for i in range(n):
                res = max(res, dfs(i))
            return res

        result = top_down(nums)

        return result
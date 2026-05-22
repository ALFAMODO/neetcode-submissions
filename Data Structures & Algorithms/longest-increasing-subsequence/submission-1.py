class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        #dp = [1] * len(nums)
        #for i in range(1, len(nums)):
            #for j in range(i):
                #if nums[i] > nums[j]:
                    #dp[i] = max(dp[i], dp[j] + 1)

        #return max(dp)

        #### Top Down ####

        n = len(nums)
        dp = [-1] * n

        def dfs(i):
            if dp[i] != -1:
                return dp[i]

            LIS = 1
            for j in range(i+1, n):
                if nums[i] < nums [j]:
                    LIS = max(LIS, dfs(j)+1)
                
            dp[i] = LIS
            return LIS


        return max(dfs(i) for i in range(n))
        
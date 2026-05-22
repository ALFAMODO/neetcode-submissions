class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)

        dp_max = [0] * n
        dp_min = [0] * n

        dp_max[0] = nums[0]
        dp_min[0] = nums[0]

        max_sum = nums[0]
        min_sum = nums[0]

        total_max=nums[0]
        for i in range(1, n):
            dp_max[i] = max(nums[i], nums[i] + dp_max[i-1])
            dp_min[i] = min(nums[i], nums[i] + dp_min[i-1])

            max_sum = max(max_sum, dp_max[i])
            min_sum = min(min_sum, dp_min[i])

            total_max += nums[i]
        
        if max_sum < 0:
            return max_sum
        
        return max(max_sum, total_max - min_sum)
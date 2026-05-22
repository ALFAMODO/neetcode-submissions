class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxs, curs = nums[0], 0
        for num in nums:
            if curs < 0:
                curs = 0
            curs += num
            maxs= max(maxs, curs)
        return maxs
class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums):
        l0, l1 = 0, 0
        for n in nums:
            total = max(n + l0, l1)
            l0 = l1
            l1 = total

        return l1        
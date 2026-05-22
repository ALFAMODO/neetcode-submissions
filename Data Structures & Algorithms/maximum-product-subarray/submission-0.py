class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cmin = cmax = res = nums[0]

        for i in nums[1:]:
            temp = cmax
            cmax = max(i, i*cmax, i*cmin)
            cmin = min(i, i*temp, i*cmin)
            res = max(res, cmax)

        return res
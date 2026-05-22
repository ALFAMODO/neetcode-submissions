class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            complacent = target - num
            if complacent in seen:
                return [seen[complacent], i]
            
            seen[num] = i
                

        
        
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr = 0
        prefix = {0:1}
        count = 0
        for i in nums:
            curr += i

            if (curr - k) in prefix:
                count += prefix[curr - k]
            
            prefix[curr] = 1 + prefix.get(curr, 0)

        return count

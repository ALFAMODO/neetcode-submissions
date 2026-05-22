from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l=defaultdict(int)

        for i in nums:
            l[i] += 1   
        
        sorted_items = sorted(l.items(), key=lambda x: x[1], reverse =True)

        top_k = [item[0] for item in sorted_items[:k]]
        return top_k
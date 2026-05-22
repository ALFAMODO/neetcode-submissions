import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Turn list into a max heap
        heapq.heapify_max(stones)

        # Keep smashing while we have at least two stones
        while len(stones) > 1:
            y = heapq.heappop_max(stones)  # largest
            x = heapq.heappop_max(stones)  # second largest

            if y != x:
                heapq.heappush_max(stones, y - x)

        # If one stone remains, return it; else return 0
        return stones[0] if stones else 0

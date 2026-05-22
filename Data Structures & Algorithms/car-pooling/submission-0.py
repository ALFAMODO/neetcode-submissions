class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key= lambda x:x[1])

        cur= 0
        heap = []

        for pas, s, e in trips:
            while heap and heap[0][0] <= s:
                cur -= heapq.heappop(heap)[1]
            
            cur += pas

            if cur > capacity:
                return False

            heapq.heappush(heap, (e, pas))
        return True
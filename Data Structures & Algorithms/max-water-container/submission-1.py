class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n= len(heights)
        l=0
        r=n-1
        full = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            full = max(area, full)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        
        return full


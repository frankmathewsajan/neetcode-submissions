class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0 , n - 1
        A = 0
        while l < r:
            smallest = min(heights[l], heights[r])
            area = smallest * (r - l)
            A = max(A, area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1    
                
            
        return A    
            
        
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0

        left = 0
        right = len(heights)-1
        max_area = 0

        for i in range(len(heights)):
            area = (right-left)*min(heights[left], heights[right])
            if area > max_area:
                max_area = area
            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] <= heights[right]:
                left +=1 
        
        return max_area
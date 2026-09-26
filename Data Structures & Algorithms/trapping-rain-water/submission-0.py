class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        left = 0
        right = len(height)-1
        water = 0

        left_max = 0
        right_max = 0

        for i in range(len(height)):
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)

            if left_max <= right_max:
                left_max = max(height[left], left_max)
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(height[right], right_max)
                water += right_max - height[right] 
                right -= 1

        return water
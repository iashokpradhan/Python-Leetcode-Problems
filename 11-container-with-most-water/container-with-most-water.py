class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_v = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            # Calculate the current area
            width = right - left
            current_height = min(height[left], height[right])
            area = width * current_height
            
            # Update global maximum
            max_v = max(max_v, area)
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_v
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            # Calculate the area between the two pointers
            area = min(height[left], height[right]) * (right - left)
            # Update max_area if the calculated area is greater
            max_area = max(max_area, area)

            # Move the pointer with the smaller height towards the center
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# Test the function
solution = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print("Maximum amount of water:", solution.maxArea(height))

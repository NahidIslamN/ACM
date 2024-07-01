from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        covered = 0
        i = 0

        while covered < n:
            if i < len(nums) and nums[i] <= covered + 1:
                covered += nums[i]
                i += 1
            else:
                patches += 1
                covered += covered + 1

        return patches

# Example usage:
solution = Solution()
nums =[1,5,10]
n = 20
print(solution.minPatches(nums, n))  # Output: 1

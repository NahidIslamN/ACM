from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        count_diff = 0
        count_map = {0: -1}

        for i in range(len(nums)):
            if nums[i] == 0:
                count_diff -= 1
            else:
                count_diff += 1

            if count_diff in count_map:
                max_length = max(max_length, i - count_map[count_diff])
            else:
                count_map[count_diff] = i

        return max_length

# Example usage:
solution = Solution()
nums = [0, 1]
print(solution.findMaxLength(nums))  # Output: 2


'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # create a dictionary to store the indices of each number
        indices = {}
        
        # iterate over the array of numbers
        for i, num in enumerate(nums):
            # check if the difference between target and current number exists in the dictionary
            if target - num in indices:
                # return the indices of the two numbers
                return [indices[target - num], i]
            
            # add the current number and its index to the dictionary
            indices[num] = i
        
        # if no solution is found, return an empty array
        return []
obj=Solution()
print(obj.twoSum([10,20,30],30))

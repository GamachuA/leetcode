# Given an array of integers nums and an integer target, return the indices of the
# two numbers such that they add up to target. Each input has exactly one solution,
# and you may not use the same element twice. The answer can be returned in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # dictionary to store number -> index
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i


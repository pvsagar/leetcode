'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 1:
            return False
        temp ={}
        for i in range(len(nums)):
            if nums[i] in temp:
                # print(temp)
                return [temp[nums[i]], i]
            else:
                # print(target - nums[i])
                temp[target - nums[i]] = i

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.3
"""

class Solution:
    def twoSum(self, nums, target):
        count = 0
        tam = len(nums)
        for i, num in enumerate(nums):
            count+=1
            if nums[i] + nums[i+1] == target and (i+1) <= (tam-1):
                print(nums[i])
                print(nums[i+1])
                print('bateu')
                print(i, i+1)
                break
            elif count < tam:
                print('Não bateu')

numbers = [1, 2, 3, 4]
target_1 = 8
run = Solution()
run.twoSum(numbers, target_1)
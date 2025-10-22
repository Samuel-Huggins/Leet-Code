# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
class Solution:
    def runningSum(self, nums):
        result = []
        total = 0
        for num in nums:
            total += num
            result.append(total)
        return result
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        missing = [0] * 2
        for num in nums:
            if num != nums[num]:
                return (missing[1] = nums[num]) + (missing[2] = num) 
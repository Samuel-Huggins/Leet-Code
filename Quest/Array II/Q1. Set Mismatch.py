class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        missing=[0] *2
        for i in range(len(nums)):
            if nums[i] != i+1:
                missing[0] = nums[i]
                missing[1] = i+1
        return missing
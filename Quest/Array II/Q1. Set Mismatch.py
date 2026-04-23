class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set()
        dupe = 0
        missing = [0] * 2
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                dupe = nums[i]

        for i in range(1, len(nums) + 1):
            if i not in seen:
                missing[1] = i

        missing[0] = dupe
        return missing
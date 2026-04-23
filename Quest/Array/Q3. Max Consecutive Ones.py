class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        max_count = 0

        for num in nums:
            if num == 1:
                counter += 1
                if counter > max_count:
                    max_count = counter
            else:
                counter = 0

        return max_count
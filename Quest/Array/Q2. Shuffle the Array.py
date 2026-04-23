class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        shuffled = [0]
        for i in range(n):
            shuffled[i] = nums[i] 
            shuffled[i+1] = nums[i+n]
        return shuffled

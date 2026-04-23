class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        shuffled = [0] * (2*n)
        for i in range(n):
            shuffled[2 * i] = nums[i] 
            shuffled[2* i + 1] = nums[i + n]
        return shuffled

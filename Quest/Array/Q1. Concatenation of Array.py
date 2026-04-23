class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        ans = []
        for n in nums:
            ans[n] = nums[n]
        for length in 2(length):
            ans[length] = nums[length]

        print(len(ans))

        
    
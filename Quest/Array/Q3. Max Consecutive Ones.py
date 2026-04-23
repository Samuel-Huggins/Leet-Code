class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        max = 0
        length = len(nums)
        for x in range(length):
            for y in range(length-1):
                if nums[x] == 1 and nums[y+1] == 1:
                    counter += 1
                    print(counter)
                    if counter > max:
                        max = counter
            counter = 0
        return max
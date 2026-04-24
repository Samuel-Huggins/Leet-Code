class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        looplength = 0
        if len(word1) <= len(word2):
            looplength = len(word2)
        else:
            looplength = len(word1)
        word3 = ("" * looplength)
        for i in range(0, looplength):
            word3 = word3 + (word1[i])
            word3 = word3 + (word2[i])
        return word3
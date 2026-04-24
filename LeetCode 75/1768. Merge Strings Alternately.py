class Solution(object):
    def mergeAlternately(self, word1, word2):
        word3 = ""
        min_len = min(len(word1), len(word2))

        for i in range(min_len):
            word3 += word1[i]
            word3 += word2[i]

        word3 += word1[min_len:]
        word3 += word2[min_len:]

        return word3
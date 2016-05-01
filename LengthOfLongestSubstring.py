class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        pointer = length = 0
        dictionary = {}
        for i, element in enumerate(s):
            if element in dictionary:
                if pointer <= dictionary[element]:
                    length = max(length, i-pointer)
                    pointer = dictionary[element]+1
            dictionary[element] = i
        return max(length, len(s) - pointer)
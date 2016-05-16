class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        head = 0
        maxLength = 0
        for i in xrange(len(s)):
            if s[i] not in d:
                d[s[i]] = i
            else:
                if head < d[s[i]]:
                    maxLength = max(maxLength, i - head)
                    head = d[s[i]]+1
        return max(maxLength, len(s) - head)

testCase = Solution()
print(testCase.lengthOfLongestSubstring("abccadcd"))
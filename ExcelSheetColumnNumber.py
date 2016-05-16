class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in xrange(len(s)-1, -1, -1):
            result += (1+ord(s[i]) - ord("A")) * (26**(len(s) - 1 - i))
        return result

testCase = Solution()
print(testCase.titleToNumber("AA"))

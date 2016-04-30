class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""

        while n > 0:
            n -= 1
            temp = n%26
            result = chr(ord('A') + temp) + result
            n /= 26
        return result


testCase = Solution()
print(testCase.convertToTitle(28))
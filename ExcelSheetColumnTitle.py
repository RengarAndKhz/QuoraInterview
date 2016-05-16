class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        while n > 0:
            n -= 1
            result = chr(ord("A") + n%26)
            n /= 26
        return result
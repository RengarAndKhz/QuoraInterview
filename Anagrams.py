
# O(N!)
class Solution(object):
    def anagrams(self, s):
        result = []
        self.helper(s, result, "")
        return result

    def helper(self, s, result, temp):
        if len(s) == 0:
            result.append(temp)
            return
        for i in xrange(len(s)):
            if i > 0 and s[i] == s[i-1]: continue
            self.helper(s[:i]+s[i+1:], result, temp+s[i])


testCase = Solution()
print(testCase.anagrams("abcc"))
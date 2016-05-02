# O(2^n)
class Solution(object):
    def subsetProduct(self, nums):
        result = []
        self.helper(nums, 0, 1, result)
        return result[1:]
    def helper(self, nums, index, path, result):
        result.append(path)
        for i in xrange(index, len(nums)):
            self.helper(nums, i+1, path*nums[i], result)


testCase = Solution()
print(testCase.subsetProduct([2,3,5,7]))
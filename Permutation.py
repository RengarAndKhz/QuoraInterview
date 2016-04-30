class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.helper(nums, [], result)
        return result

    def helper(self, nums, temp, result):
        if len(nums) == 0:
            result.append(temp)
        for i in xrange(len(nums)):
            self.helper(nums[:i] + nums[i+1:], temp+[nums[i]], result)

testCase = Solution()
print(testCase.permute([1,2,3]))

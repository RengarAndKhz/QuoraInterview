class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in sorted(nums):
            result += [element + [num] for element in result]
        return result

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(sorted(nums), [], result)
        return result
    def dfs(self, nums, path, result):
        result.append(path)
        for i in xrange(nums):
            if i > 0 and nums[i] == nums[i-1]: continue
            self.dfs(nums[i+1:], path + [nums[i]], result)
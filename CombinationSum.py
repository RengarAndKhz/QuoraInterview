class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.helper(candidates, target, result, [])
        return result

    def helper(self, candidate, target, result, path):
        if target < 0: return
        if target == 0: result.append(path)
        for i in xrange(len(candidate)):
            if i>0 and candidate[i] == candidate[i-1]:continue
            self.helper(candidate[i+1:], target-candidate[i], result, path + [candidate[i]])

testCase = Solution()
print(testCase.combinationSum([1,2,2,3], 5))
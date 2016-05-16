import numpy as np
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if i == 0 and j == 0: continue
                if i != 0 and j == 0: grid[i][j] += grid[i-1][j]
                if i == 0 and j != 0: grid[i][j] += grid[i][j-1]
                if i != 0 and j != 0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        print(np.matrix(grid))
        return grid[len(grid)-1][len(grid[0])-1]

testCase = Solution()
testCase.minPathSum([[1,2],[1,1]])
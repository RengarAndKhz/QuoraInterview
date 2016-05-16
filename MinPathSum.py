class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in xrange(len(grid[0])):
            for j in xrange(len(grid)):
                if i == 0 and j == 0: continue
                if i != 0 and j == 0: grid[j][i] += grid[j][i-1]
                if i == 0 and j != 0: grid[j][i] += grid[j-1][i]
                if i != 0 and j != 0:
                    grid[j][i] += min(grid[j-1][i], grid[j][i-1])
        return grid[len(grid)-1][len(grid[0])-1]
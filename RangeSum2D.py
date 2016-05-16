import copy
import numpy as np
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.matrix = copy.deepcopy(matrix)
        print(np.matrix(self.matrix))
        self.getsum(self.matrix)
        print(np.matrix(self.matrix))
    def getsum(self, matrix):
        if len(matrix) > 0:
            for i in xrange(len(matrix[0])):
                for j in xrange(len(matrix)):
                    if j > 0:
                        matrix[j][i] += matrix[j-1][i]
            for i in xrange(len(matrix)):
                for j in xrange(len(matrix[0])):
                    if j > 0:
                        matrix[i][j] += matrix[i][j-1]


    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.matrix[row2][col2] - (self.matrix[row2][col1-1] if col1 > 0 else 0) - (self.matrix[row1-1][col2] if row1 > 0 else 0) + (self.matrix[row1-1][col1-1] if row1>0 and col1 > 0 else 0)


testCase = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
print(testCase.sumRegion(2,1,4,3))

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
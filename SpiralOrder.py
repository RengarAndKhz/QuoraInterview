class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0: return []
        result = []
        rowStart = 0
        rowEnd = len(matrix[0]) - 1
        colStart = 0
        colEnd = len(matrix) - 1
        while rowStart <= rowEnd and colStart <= colEnd:
            for i in xrange(rowStart, rowEnd+1):
                result.append(matrix[colStart][i])
            colStart += 1
            for i in xrange(colStart, colEnd+1):
                result.append(matrix[i][rowEnd])
            rowEnd -= 1
            if colStart <= colEnd:
                for i in xrange(rowEnd, rowStart-1, -1):
                    result.append(matrix[colEnd][i])
                colEnd -= 1
            if rowStart <= rowEnd:
                for i in xrange(colEnd, colStart-1, -1):
                    result.append(matrix[i][rowStart])
                rowStart += 1
        return result
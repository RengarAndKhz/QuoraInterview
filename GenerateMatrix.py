class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0: return []
        matrix = [[0*n] for _ in xrange(n)]
        rowStart = 0
        rowEnd = n
        colStart = 0
        colEnd = n
        insertVal = 1
        while rowStart <= rowEnd and colStart <= colEnd:
            for i in xrange(rowStart, rowEnd+1):
                matrix[colStart][i] = insertVal
                insertVal += 1
            colStart += 1
            for i in xrange(colStart, colEnd+1):
                matrix[i][rowEnd] = insertVal
                insertVal += 1
            rowEnd -= 1
            if colStart <= colStart:
                for i in xrange(rowEnd, rowStart-1, -1):
                    matrix[colEnd][i] = insertVal
                    insertVal += 1
                colEnd -= 1
            if rowStart <= rowEnd:
                for i in xrange(colEnd, colStart-1, -1):
                    matrix[i][rowStart] = insertVal
                    insertVal += 1
                rowStart += 1
        return matrix
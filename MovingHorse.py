import numpy as np
class Solution(object):
    def __init__(self):
        self.chessboard = [[-1 for _ in xrange(8)] for _ in xrange(8)]
        #print(self.chessboard)


    def setHorse(self, i, j):
        self.chessboard[i][j] = 0

    def moveHorse(self, i, j):
        offset = self.chessboard[i][j]
        result = []
        if i-1 >= 0 and j - 2 >= 0 and self.chessboard[i-1][j-2] == -1:
            self.chessboard[i-1][j-2] = offset+1
            result.append((i-1, j-2))
        if i - 2 >= 0 and j - 1 >= 0 and self.chessboard[i-2][j-1] == -1:
            self.chessboard[i-2][j-1] = offset+1
            result.append((i-2, j-1))
        if i-2 >= 0 and j+1 < 8 and self.chessboard[i-2][j+1] == -1:
            self.chessboard[i-2][j+1] = offset+1
            result.append((i-2, j+1))
        if i-1 >= 0 and j+2 < 8 and self.chessboard[i-1][j+2] == -1:
            self.chessboard[i-1][j+2] = offset+1
            result.append((i-1, j+2))
        if i+1 < 8 and j-2 >= 0 and self.chessboard[i+1][j-2] == -1:
            self.chessboard[i+1][j-2] = offset+1
            result.append((i+1, j-2))
        if i+2 < 8 and j-1 >= 0 and self.chessboard[i+2][j-2] == -1:
            self.chessboard[i+2][j-1] = offset+1
            result.append((i+2, j-1))
        if i+1 < 8 and j+2 < 8 and self.chessboard[i+1][j+2] == -1:
            self.chessboard[i+1][j+2] = offset+1
            result.append((i+1, j+2))
        if i+2 < 8 and j+1 < 8 and self.chessboard[i+2][j+1] == -1:
            self.chessboard[i+2][j+1] = offset+1
            result.append((i+2, j+1))
        print(np.matrix(self.chessboard), (i,j))
        return result
    def fill(self, i, j):
        self.setHorse(i, j)
        queue = [(i, j)]
        while queue:
            x, y = queue.pop(0)
            queue += self.moveHorse(x,y)
        #print(self.chessboard)

testCase = Solution()
testCase.fill(0,0)


class Solution(object):
    def solveNQueens(self, n):
        def dfs(board, row):
            if row == n:
                result.append(['.' * x + 'Q' + '.' * (n - 1 - x) for x in board])
                return
            for x in set_n - set(board):
                # check diagonal conflict
                if all(row - i != abs(x - y) for i, y in enumerate(board[:row])):
                    board[row] = x
                    dfs(board, row + 1)
                    board[row] = '.'

        result, set_n = [], {i for i in xrange(n)}
        dfs(['.'] * n, 0)
        return result

testCase = Solution()
print(testCase.solveNQueens(4))


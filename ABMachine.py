'''BSF SOLCER'''
class Solution(object):
    def dsfSolver(self, target):
        x,y = 1,1
        layer = 0
        queue = [("A", x, y, layer+1), ("B", x, y, layer+1)]

        while x != target and y != target:
            operation, x, y, layer = queue.pop(0)
            if operation == "A":
                x += y
            else:
                y += x
            queue.append(("A", x, y, layer+1))
            queue.append(("B", x, y, layer+1))
        return layer

testCase = Solution()
print(testCase.dsfSolver(10))


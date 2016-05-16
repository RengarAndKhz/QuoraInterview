import sys
class Solution(object):
    def __init__(self):
        self.result = sys.maxint
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.dfs(sorted(coins, reverse=True), amount, 0)
        return self.result if self.result != sys.maxint else -1

    def dfs(self, coins, amount, result):

        if amount == 0:
            #print(result)
            self.result = min(self.result, result)
            return
        for i in xrange(len(coins)):
            if coins[i] <= amount < coins[i] *(self.result - result):
                self.dfs(coins[i:], amount-coins[i], result+1)


testCase = Solution()
print(testCase.coinChange([186,419,83,408], 6249))
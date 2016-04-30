import math
class Solution(object):
    def twoMissingNumber(self, nums, n):
        result = []
        sumN = n*(n+1)/2
        sumNums = sum(nums)
        mulN = math.factorial(n)
        mulNums = 1
        for num in nums:
            mulNums *= num
        # x + y
        xAddy = sumN - sumNums
        # x * y
        xMuly = mulN / mulNums
        for num in range(1,n+1):
            if (num**2 - xAddy*num + xMuly) == 0:
                result.append(num)
        return result

testCase = Solution()
print(testCase.twoMissingNumber([], 0))
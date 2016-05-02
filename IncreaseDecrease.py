class Solution(object):
    def increaseDecrease(self, nums):
        result = 0
        sum = 0
        flag = True
        for i, num in enumerate(nums):
            sum += self.symbol(i, flag) * num
            if sum < 0:
                result = max(result, sum - self.symbol(i, flag)*num)
                flag = not flag
                sum = -sum
        return max(sum, result)

    def symbol(self, i, flag):
        if flag:
            return -1 if i%2 == 0 else 1
        else:
            return 1 if i%2 == 0 else -1

testCase = Solution()
print(testCase.increaseDecrease([1,2,3]))
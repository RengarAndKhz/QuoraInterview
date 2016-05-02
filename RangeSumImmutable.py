class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sumList = [0]
        for num in nums:
            self.sumList += [self.sumList[-1]+num]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumList[j+1] - self.sumList[i]



# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
testCase = NumArray([-2,0,3,-5,2,-1])
print(testCase.sumList)
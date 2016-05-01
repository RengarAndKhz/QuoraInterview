class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        invertNum = 0
        for i in xrange(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                invertNum = i
                break
        else:
            sorted(nums)
        invertNum2 = 0
        for i in xrange(len(nums)-1, -1, -1):
            if nums[i] > nums[invertNum]:
                invertNum2 = i
                break
        nums[invertNum], nums[invertNum2] = nums[invertNum2], nums[invertNum]
        nums[invertNum+1:] = sorted(nums[invertNum+1:])

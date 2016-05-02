class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        maxEndingHere = 0
        maxSoFar = nums[0]
        for num in nums:
            maxEndingHere = max(num, maxEndingHere + num)
            maxSoFar = max(maxSoFar, maxEndingHere)
        return maxSoFar
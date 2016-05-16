class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = 0
        now = nums[0]
        for i in xrange(1, len(nums)):
            last, now = now, max(last + nums[i], now)
        return now

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        rotateTimes = k%n
        nums[:] = nums[(n-rotateTimes):] + nums[:(n-rotateTimes)]
        '''A little important thing to be cautious:

nums[:] = nums[n-k:] + nums[:n-k]
can't be written as:

nums = nums[n-k:] + nums[:n-k]
on the OJ.

The previous one can truly change the value of old nums, but the following one just changes its reference to a new nums not the value of old nums.'''
import heapq
h = ["a", "b", "c"]
heapq.heapify(h)
heapq.heappop()
print(h)
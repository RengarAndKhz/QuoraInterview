class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2])
        print(nums[:half][::-1])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

nums = [1,2,3,4,5,6]
testCase = Solution()
testCase.wiggleSort(nums)
print(nums)
print(nums[::2])
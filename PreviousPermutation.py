class Solution(object):
    def previousePermutation(self, nums):
        pointer1 = 0
        for i in xrange(len(nums)-2, -1, -1):
            if nums[i] > nums[i+1]:
                pointer1 = i
                break
        else:
            nums.sort(reverse=True)
            return
        pointer2 = 0
        for i in xrange(len(nums)-1, -1, -1):
            if nums[i] < nums[pointer1]:
                pointer2 = i
                break
        nums[pointer1], nums[pointer2] = nums[pointer2], nums[pointer1]
        nums[pointer1+1:] = sorted(nums[pointer1+1:], reverse=True)

testCase = Solution()
nums = [1,2,4,5,3]
testCase.previousePermutation(nums)
print(nums)
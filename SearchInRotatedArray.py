class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        head = 0
        tail = len(nums) - 1
        while head <= tail:
            mid = (head + tail) / 2
            if nums[mid] == target: return mid
            if nums[head] <= nums[mid]:
                if nums[head] <= target <= nums[mid]:
                    tail = mid -1
                else:
                    head = mid + 1
            else:
                if nums[mid] <= target <= nums[tail]:
                    head = mid + 1
                else:
                    tail = mid -1
        return -1

testCase = Solution()
print(testCase.search([1,4,6,2,3,8], 3))
import heapq
'''quick select O(n), min heap sort can be O(k + (n-k)log(k))'''
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''if k > len(nums):
            return
        temp = []
        for num in nums:
            temp.append(-1 * num)
        h = heapq.heapify(temp)
        result = 0
        for _ in xrange(k):
            result = heapq.heappop(h)
        return -1 * result'''
        return self.quickSelect(nums, 0, len(nums) - 1, len(nums) - k + 1)

    def quickSelect(self, nums, head, tail, k):
        pivot = nums[tail]
        i, j = head, tail - 1
        while i <= j:
            if nums[i] > pivot:
                self.swap(nums, i, j)
                j -= 1
            else: i += 1
        self.swap(nums, i, tail)
        m = i - head + 1
        if m == k: return nums[i]
        elif m < k: return self.quickSelect(nums, i + 1, tail, k - m)
        else: return self.quickSelect(nums, head, i-1, k)

    def swap(self, list, i, j):
        temp = list[i]
        list[i] = list[j]
        list[j] = temp
testCase = Solution()
print(testCase.findKthLargest([3,1,2,4], 2))
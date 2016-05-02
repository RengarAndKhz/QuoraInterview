class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        pointer = 0
        for i in xrange(len(nums2)):
            while nums1[pointer] < nums2[i]:
                if pointer < len(nums1):
                    pointer += 1
                else:
                    nums1 += nums2[i:]
                    return
            nums1.insert(pointer, nums2[i])

nums1 = [1, 5, 8]
nums2 = [2,3, 4, 6, 8]
testCase = Solution()
testCase.merge(nums1, 3, nums2, 5)
print(nums1)
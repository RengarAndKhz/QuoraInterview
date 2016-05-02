import collections, copy
class Solution(object):
    def solver(self, nums):
        d = collections.defaultdict(int)
        for num in nums:
            d[num] += num
        keys = copy.copy(sorted(d.keys()))
        #print(keys)
        last = now = 0
        for i in xrange(len(keys)):
            if i == 0 or keys[i] == keys[i-1]+1:
                last, now = now, max(last+d[keys[i]], now)
            else:
                last, now = now, now + d[keys[i]]

        return now

testCase = Solution()
print(testCase.solver([1,3,4,7]))


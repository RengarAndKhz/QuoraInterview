#O(NM) size of the matrix multiply size of the string
import collections
class Solution(object):
    '''def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = collections.defaultdict(list)
        for s in strs:
            print(sorted(s))
            d[tuple(sorted(s))].append(s)
        #result = copy.deepcopy(d.values())
        for subList in d.values():
            subList.sort()
        return sorted(d.values())'''

    def groupAnagrams(self, strs):
        d = collections.defaultdict(list)
        for s in strs:
            d[self.key(s)].append(s)
        for item in d.values():
            item.sort()
        return sorted(d.values())


    def key(self, s):
        list = [0]*26
        for i in xrange(len(s)):
            list[ord(s[i]) - ord("a")] += 1
        return tuple(list)
        #return tuple([(s[i], i) for i in xrange(len(s))])
    '''Or use 26 primes product as hash code'''
testCase = Solution()
print(testCase.groupAnagrams(["ape","and","cat"]))
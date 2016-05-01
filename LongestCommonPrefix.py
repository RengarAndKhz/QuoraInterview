class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        temp = zip(*strs)
        for item in temp:
            if item.count(item[0]) == len(item):
                result += item[0]
            else:
                break
        return result

class Solution(object):
    def sovler(self, nums):
        dictionary = {}
        pointer = length = 0
        for i, element in enumerate(nums):
            if element not in dictionary:
                if len(dictionary) < 2:
                    dictionary[element] = i
                else:
                    length = max(length, i - pointer)
                    temp = dictionary.pop(dictionary.keys()[0]) if dictionary[dictionary.keys()[0]] < dictionary[dictionary.keys()[1]] else dictionary.pop(dictionary.keys()[1])
                    pointer = temp + 1
                    dictionary[element] = i
            else:
                dictionary[element] = i
        return max(length, len(nums) - pointer)


testCase = Solution()
print(testCase.sovler("abcddccssss"))

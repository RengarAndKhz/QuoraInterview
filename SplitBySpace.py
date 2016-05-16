class Solution(object):
    def solver(self, string):
        result = []
        pointer = 0
        word = ""
        while pointer < len(string):
            if string[pointer] == " ":
                if word != "":
                    result.append(word)
                    word = ""
            elif string[pointer] == "\"":
                pointer += 1
                while string[pointer] != "\"":
                    word += string[pointer]
                    pointer += 1
                if word != "":
                    result.append(word)
                    word = ""
            else:
                word += string[pointer]
            pointer += 1
        if word != "":
            result.append(word)
        return result




testCase = Solution()
print(testCase.solver(" a \"ba caa\" "))
print("ab cd \"bacaa\" ab")

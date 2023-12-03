class Solution:
    def printVertically(self, s: str) -> List[str]:
        maximum_len = 0
        output = []
        s = s.split()
        for val in s:
            if len(val) > maximum_len:
                maximum_len = len(val)
        for i in range(maximum_len):
            temp = ""
            for j in range(len(s)):
                if i >= len(s[j]):
                    temp += " "
                else:
                    temp += s[j][i]
            output.append(temp.rstrip())
        return output
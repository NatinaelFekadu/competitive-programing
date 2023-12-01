class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        i = num = 0
        while i < len(s):
            if i < len(s) - 1 and (s[i+1] == "V" or s[i+1] == "X") and s[i] == "I":
                num += hashmap[s[i+1]] - 1
                i += 2
            elif i < len(s) - 1 and (s[i+1] == "L" or s[i+1] == "C") and s[i] == "X":
                num += hashmap[s[i+1]] - 10
                i += 2
            elif i < len(s) - 1 and (s[i+1] == "D" or s[i+1] == "M") and s[i] == "C":
                num += hashmap[s[i+1]] - 100
                i += 2
            else:
                num += hashmap[s[i]]
                i += 1
        return num
            

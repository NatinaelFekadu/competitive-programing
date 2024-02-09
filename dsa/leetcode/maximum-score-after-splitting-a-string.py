class Solution:
    def maxScore(self, s: str) -> int:
        prefix = [0 for _ in range(len(s) + 1)]
        for i in range(len(s)):
            if i == 0:
                continue
            elif s[i-1] == "0":
                prefix[i] = prefix[i-1] + 1
            else:
                prefix[i] = prefix[i-1]
        suffix = [0 for _ in range(len(s) + 1)]
        for i in range(len(s), -1, -1):
            if i == len(s):
                continue
            elif s[i] == "1":
                suffix[i] = suffix[i+1] + 1
            else:
                suffix[i] = suffix[i+1]
        print(prefix)
        print(suffix)
        max_value = 0
        for i in range(1, len(s)):
            max_value = max(max_value, prefix[i] + suffix[i])
        return max_value
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        window = Counter()
        left = 0
        res = ""
        min_win = float("inf")
        def isValid(dict1, dict2):
            if len(dict2) > len(dict1):
                return False
            for key, value in dict2.items():
                if key not in dict1 or dict1[key] < value:
                    return False
            return True
        for right, char in enumerate(s):
            window[char] += 1            
            while isValid(window, count_t):
                if right - left + 1 < min_win:
                    res  = s[left:right+1]
                    min_win = right - left + 1
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
        return res
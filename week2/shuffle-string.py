class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled_string = list(s)
        for i in indices:
            shuffled_string[indices[i]] = s[i]
        return "".join(shuffled_string)
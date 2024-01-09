class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pCount = Counter(p)
        sCount = Counter(s[:len(p)])
        l = 0
        res = [0] if sCount == pCount else []
        for r in range(len(p),len(s)):
            sCount[s[l]] -= 1
            if sCount[s[l]] == 0:
                del sCount[s[l]]
            sCount[s[r]] = sCount.get(s[r],0) + 1
            l += 1
            if sCount == pCount:
                res.append(l)
        return res
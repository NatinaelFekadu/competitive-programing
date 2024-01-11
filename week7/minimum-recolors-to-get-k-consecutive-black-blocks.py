class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left, right = 0, k
        colors = Counter(blocks[:k])
        res = colors["W"]
        while right < len(blocks):
            colors[blocks[left]] -= 1
            colors[blocks[right]] += 1
            left, right = left + 1, right + 1
            res = min(res,colors["W"])
        return res if res != float('inf') else 0
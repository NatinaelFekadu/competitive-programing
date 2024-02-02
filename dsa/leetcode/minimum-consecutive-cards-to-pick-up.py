class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        window = {}
        left = 0
        res = float("inf")
        for right,val in enumerate(cards):
            if val in window:
                res = min(res, right - window[val] + 1)
                left += 1
                window[val] = right
            window[val] = right
        return res if res != float("inf") else -1
            
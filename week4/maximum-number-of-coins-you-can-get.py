class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_res = 0
        j = 2
        for i in range(0,len(piles),3):
            max_res += piles[len(piles) - j]
            j += 2
        return max_res
        
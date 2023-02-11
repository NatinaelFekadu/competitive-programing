class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = 0
        i = len(piles)-2
        j = -1
        while(i>j):
            ans+=piles[i]
            j+=1
            i-=2
        return ans

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        if costs[0] > coins:
            return 0
        i = 0
        while i < len(costs) and coins > 0:
            if coins < costs[i]:
                break
            coins -= costs[i]
            count+=1
            i+=1
        return count
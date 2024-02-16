class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        min_moves = 0
        while target > 1 and maxDoubles > 0:
            if target % 2 == 1:
                min_moves += 2
            else:
                min_moves += 1
            target //= 2
            maxDoubles -= 1
        return target - 1 + min_moves
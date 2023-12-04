class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        my_dist = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            y = abs(target[1] - ghost[1])
            x = abs(target[0] - ghost[0])
            if x + y <= my_dist:
                return False
        return True
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        min_integer = float("inf")
        front_dict = Counter(fronts)
        back_dict = Counter(backs)
        for i in range(len(fronts)):
            if fronts[i] != backs[i]:
                if front_dict[fronts[i]] == 1:
                    min_integer = min(min_integer,fronts[i])
                if back_dict[backs[i]] == 1:
                    min_integer = min(min_integer,backs[i])
                front_dict[fronts[i]] -= 1
                back_dict[backs[i]] -= 1

        return min_integer if min_integer != float("inf") else 0
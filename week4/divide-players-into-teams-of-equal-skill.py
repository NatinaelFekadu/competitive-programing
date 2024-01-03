class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        p1 = 0
        p2 = len(skill) - 1
        init_sum = skill[p1] + skill[p2]
        chemistry = 0
        while p1 < p2:
            if skill[p1] + skill[p2] == init_sum:
                chemistry += (skill[p1] * skill[p2])
            else:
                return -1
            p1 += 1
            p2 -= 1
        return chemistry

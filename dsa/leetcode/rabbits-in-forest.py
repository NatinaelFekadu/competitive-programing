class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        min_rabbits = 0
        for val in count:
            c = ceil(count[val] / (val + 1))
            min_rabbits += (c * (val + 1))
        return min_rabbits
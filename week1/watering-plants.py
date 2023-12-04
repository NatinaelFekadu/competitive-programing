class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        temp = capacity
        for i in range(len(plants)):
            if capacity - plants[i] < 0:
                steps += (2 * len(plants[:i]))
                capacity = temp
            capacity -= plants[i]
            steps += 1
        return steps
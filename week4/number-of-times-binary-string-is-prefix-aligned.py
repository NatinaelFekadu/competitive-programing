class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        max_value = count = 0
        for i in range(len(light)):
            if max_value < light[i]:
                max_value = light[i]
            if max_value == i + 1:
                count += 1
        return count
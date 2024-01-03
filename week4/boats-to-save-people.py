class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left, right = 0, len(people) - 1
        people.sort()
        boats = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                boats += 1
                left, right = left + 1, right - 1
            else:
                right -= 1
                boats += 1
        return boats

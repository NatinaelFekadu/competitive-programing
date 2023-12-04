class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        for i in range(len(points) - 1):
            p2 = abs(points[i+1][1] - points[i][1])
            p1 = abs(points[i+1][0] - points[i][0])
            result += max(p1,p2)
        return result
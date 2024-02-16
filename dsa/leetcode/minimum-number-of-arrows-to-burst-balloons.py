class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        print(points)
        min_arrows = 1
        for i in range(len(points) - 1):
            x_start, x_end = points[i][0], points[i][1]
            next_start, next_end = points[i + 1][0], points[i + 1][1]
            if x_start == x_end or next_start <= x_end:
                if next_end < x_end:
                    points[i+1] = [x_start, next_end]
                else:
                    points[i+1] = [x_start, x_end]
                continue
            else:
                min_arrows += 1
        
        return min_arrows
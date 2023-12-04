class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        cw = ccw = 0
        end = destination
        if start > destination:
            end = start
            start = destination
        for i in range(start,end):
            cw += distance[i]
        for j in range(start - 1,-1 * (len(distance) - end) - 1,-1):
            ccw += distance[j]
        return min(cw,ccw)
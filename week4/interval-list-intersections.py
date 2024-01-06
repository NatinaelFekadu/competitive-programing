class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersections = []
        left = right = 0
        while left < len(firstList) and right < len(secondList):
            start = max(firstList[left][0],secondList[right][0])
            end = min(firstList[left][1],secondList[right][1])
            if end >= start:
                intersections.append([start,end])
            if firstList[left][1] < secondList[right][1]:
                left += 1
            elif firstList[left][1] > secondList[right][1]:
                right += 1
            else:
                left, right = left + 1, right + 1
        return intersections
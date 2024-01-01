class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        i = 0
        result = []
        distances = []
        for i in range(len(points)):
            distances.append(self.calc_distance(points[i][0],points[i][1]))
        for j in range(k):
            min_dist = min(distances)
            index = distances.index(min_dist)
            distances[index] = float("inf")
            result.append(points[index])
        return result

    def calc_distance(self,p1,p2):
        calc = p1 ** 2 + p2 ** 2
        distance = math.sqrt(calc)
        return distance
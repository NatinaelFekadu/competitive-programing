class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        counter = {}
        result = [[],[]]
        for val in matches:
            if val[0] not in counter:
                counter[val[0]] = [1,0]
            else:
                counter[val[0]][0] += 1
            if val[1] not in counter:
                counter[val[1]] = [0,1]
            else:
                counter[val[1]][1] += 1
        for key in counter:
            if counter[key][1] == 0:
                result[0].append(key)
            elif counter[key][1] == 1:
              result[1].append(key)
        result[0].sort()
        result[1].sort()
        return result
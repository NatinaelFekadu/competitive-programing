class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ln = len(temperatures)
        counts = [0] * ln
        for k in range(ln-2,-1,-1):
            j = k+1
            while True:
                if (temperatures[k] >= temperatures[j]) and counts[j] == 0:
                    break
                elif (temperatures[k] < temperatures[j]):
                    counts[k] = j-k
                    break
                else:
                    j = j + counts[j] 
        return counts

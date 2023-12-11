class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counter = dict()
        elements = len(arr)
        for val in arr:
            counter[val] = counter.get(val,0) + 1
            if counter[val] / elements > 0.25:
                return val
        
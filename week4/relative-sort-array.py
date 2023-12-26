class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        frequency = Counter(arr1)
        result = []
        for val in arr2:
            for i in range(frequency[val]):
                result.append(val)
            del frequency[val]
        r = []
        for key in frequency:
            for i in range(frequency[key]):
                r.append(key)
        r.sort()
        return result + r
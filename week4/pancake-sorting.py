class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        n = len(arr)
        for indx in range(n):
            max_value = max(arr[:n-indx])
            max_value_index = arr.index(max_value) + 1
            arr[:max_value_index] = reversed(arr[:max_value_index])
            result.append(max_value_index)

            arr[:n-indx] = reversed(arr[:n-indx])
            result.append(n-indx)
        return result
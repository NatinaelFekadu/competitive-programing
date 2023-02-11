class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        end = len(arr)
        required_size = len(arr) // 2
        arr = collections.Counter(arr)
        arr = arr.most_common(None)
        index = 0
        
        
        while (index < end and required_size > 0):
            required_size -= arr[index][1]
            index += 1
           
        return index

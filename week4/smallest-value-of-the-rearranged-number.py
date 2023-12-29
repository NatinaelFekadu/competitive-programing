class Solution:
    def smallestNumber(self, num: int) -> int:
        temp = num
        if num < 0:
            num = -1 * num
        elif num == 0:
            return 0
        num = str(num)
        arr = list(num)
        if temp > 0:
            arr.sort()
        else:
            arr.sort(reverse=True)
        i = 0
        while arr[i] == '0' and i < len(arr):
            i += 1
        arr[0],arr[i] = arr[i], arr[0]
        result = int("".join(arr))
        return result if temp > 0 else -1 * result
        
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # res = 0
        # for i in range(len(arr)):
        #     min_num = arr[i]
        #     for j in range(i, len(arr)):
        #         if arr[j] < min_num:
        #             min_num = arr[j]
        #         res += min_num
        # return res % (10 ** 9 + 7)
        arr.append(0)
        stack = []
        i = 0
        result = 0
        while i < len(arr):
            current = arr[i]
            countPrev = 1
            while stack and stack[-1][0] >= current:
                topNum, topCountPrev = stack.pop()
                result += topNum * topCountPrev * countPrev
                countPrev += topCountPrev
            stack.append((current, countPrev))
            i += 1
        return result % (10 ** 9 + 7)
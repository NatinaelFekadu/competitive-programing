class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        result = []
        for val in nums:
            if val > 0:
                positive.append(val)
            else:
                negative.append(val)
        p1,p2,turn = 0, 0, 0
        while p1 < len(positive) or p2 < len(negative):
            if turn == 0:
                result.append(positive[p1])
                p1 += 1
                turn = 1
            else:
                result.append(negative[p2])
                turn = 0
                p2 += 1
        return result
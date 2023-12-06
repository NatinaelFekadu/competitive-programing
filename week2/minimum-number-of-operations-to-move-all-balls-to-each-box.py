class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = []
        for i,box in enumerate(boxes):
            move = 0
            for j in range(len(boxes)):
                if boxes[j] == "1":
                    move += abs(i - j)
            result.append(move)
        return result
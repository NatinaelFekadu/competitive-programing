class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        div = num // 3
        return [div - 1, div , div + 1] if (div - 1) + div + (div + 1) == num else []
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for val in digits:
            num += str(val)
        num = int(num)
        num += 1
        return [int(val) for val in str(num)]
class Solution:
    def isHappy(self, n: int,count = 0) -> bool:
        previous_values = set()
        sq = 0
        while sq != 1:
            sq = self.squareSum(n)
            if sq in previous_values:
                return False
            previous_values.add(sq)
            n = sq
        return True
    def squareSum(self,n:int):
        sm = 0
        while n > 0:
            sm += (n % 10) ** 2
            n = n // 10
        return sm
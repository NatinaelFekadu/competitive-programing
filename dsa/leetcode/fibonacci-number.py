class Solution:
    def fib(self, n: int, hashmap = {}) -> int:
        if n <= 1:
            return n
        if n in hashmap:
            return hashmap[n]
        else: 
            hashmap[n] = self.fib(n-1, hashmap) + self.fib(n-2, hashmap)
        return hashmap[n]
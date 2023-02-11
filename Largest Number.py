class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comparator(x, y):
            if x+y > y+x: 
                return -1  
            else: 
                return 1 
        nums = list(map(str, nums)) 
        nums.sort(key=functools.cmp_to_k

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        hashmap = {}
        pair = 0
        for i,val in enumerate(nums):
            if val in hashmap:
                for index in hashmap[val]:
                    if index * i % k == 0:
                        pair += 1
                hashmap[val].append(i)
            elif val not in hashmap:
                hashmap[val] = [i]
        return pair
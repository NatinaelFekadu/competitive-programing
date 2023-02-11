class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        ans = 0
        for x in c:
            if k-x in c:
                ans+=min(c[x], c[k-x])
        return ans//2

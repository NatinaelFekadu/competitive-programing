class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.Counter(nums)
        sorted_d = sorted(d.items(), key=lambda kv: kv[-1], reverse=True)
        return [k for k,v in sorted_d[0:k]]

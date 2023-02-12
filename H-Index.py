class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        buckets = [0] * (N + 1)
        
        for elem in citations:
            buckets[min(elem, N)] += 1
        
        accum = list(accumulate(buckets[1:][::-1]))[::-1]  
        compar = [accum[i] >= i + 1 for i in range(N)]  
        return (compar + [0]).index(0)  

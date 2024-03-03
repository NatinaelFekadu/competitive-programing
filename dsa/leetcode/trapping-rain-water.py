class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        premax = [height[0]]*n
        for i in range(1,n):
            premax[i] = max(premax[i-1],height[i])
        postmax = [height[-1]]*n
        for i in range(n-2,-1,-1):
            postmax[i] = max(postmax[i+1],height[i])
        for i in range(0,n):
            premax[i] = abs(height[i]-premax[i])
            postmax[i] = abs(height[i]-postmax[i])
            premax[i] = min(premax[i],postmax[i])
        return sum(premax)
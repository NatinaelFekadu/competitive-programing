class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dq = collections.deque([0])
        res = 0
        
        for i in range(1, len(nums)):
            while dq and dq[0] < i - k:
                dq.popleft()
            
            nums[i] += nums[dq[0]]
            
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
    
            dq.append(i)
        
        return nums[-1]

class Solution:
    def maxSumRangeQuery(self, nums: List[int], req: List[List[int]]) -> int:
        n=len(nums)
        r=len(req)
        freq=[0 for i in range(n)]
        for i in range(r):
            freq[req[i][0]]+=1
            if(req[i][1]<n-1):
                freq[req[i][1]+1]-=1
        for i in range(n):
            if(i==0):
                continue
            freq[i]+=freq[i-1]

        freq.sort()
        nums.sort()
        ans=0
        N=1e9 + 7
        for i in range(n-1,-1,-1):
            ans+=(freq[i]*nums[i])
        return int(ans%N)
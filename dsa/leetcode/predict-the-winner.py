class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def solve(i,j,k):
            if i>j: return 0
            if k == 0:
                return max(nums[i]+solve(i+1,j,1),nums[j]+solve(i,j-1,1))
            else:
                return min(solve(i+1,j,0),solve(i,j-1,0))
        res=0
        for i in range( len(nums)):
            res += nums[i]
        ans = solve(0, len(nums)-1,0)
        print(ans)
        res -= ans
        return ans >= res
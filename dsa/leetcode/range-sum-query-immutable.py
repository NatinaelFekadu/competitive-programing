class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        for i in range(len(self.nums)):
            self.nums[i] = self.nums[i] + self.nums[i-1] if i > 0 else self.nums[i]
        self.nums.insert(0,0)
    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right + 1] - self.nums[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
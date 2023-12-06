class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left, right = 0, n
        result = []
        turn = 0
        while right < len(nums):
            if turn == 0:
                result.append(nums[left])
                left += 1
                turn = 1
            else:
                result.append(nums[right])
                right += 1
                turn = 0
        return result
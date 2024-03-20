class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(left = 0, right = len(nums) - 1, arr = nums):
            if left == right:
                return [arr[left]]
            mid = (left + right) // 2
            left_half = merge_sort(left, mid, arr)
            right_half = merge_sort(mid + 1, right, arr)
            return merge(left_half, right_half)

        def merge(left_half, right_half):
            left = right = 0
            res = []
            while left < len(left_half) and right < len(right_half):
                if left_half[left] > right_half[right]:
                    res.append(right_half[right])
                    right += 1
                else:
                    res.append(left_half[left])
                    left += 1
            return res + left_half[left:] + right_half[right:]
        return merge_sort()
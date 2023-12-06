class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than_pivot = []
        greater_than_pivot = []
        equals_pivot = []
        for val in nums:
            if val < pivot:
                less_than_pivot.append(val)
            elif val > pivot:
                greater_than_pivot.append(val)
            else:
                equals_pivot.append(val)
        return less_than_pivot + equals_pivot + greater_than_pivot
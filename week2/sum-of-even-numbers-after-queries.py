class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        result = []
        for val in nums:
            if val % 2 == 0:
                even_sum += val
        print(even_sum)
        for val,index in queries:
            if (val % 2 == 0 and nums[index] % 2 == 0):
                even_sum -= nums[index]
                nums[index] += val
                even_sum += nums[index]
            elif  (val % 2 != 0 and nums[index] % 2 != 0):
                 nums[index] += val
                 even_sum += nums[index]
            elif nums[index] % 2 == 0 and val % 2 != 0:
                 even_sum -= nums[index]
                 nums[index] += val
            else:
                 nums[index] += val
            result.append(even_sum)
        return result
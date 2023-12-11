class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
        # my_dict = dict()
        # for val in  nums:
        #     if val in my_dict:
        #         return True
        #     else:
        #         my_dict[val] = 1
        # return False
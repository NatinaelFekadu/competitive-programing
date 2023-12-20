class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        scr = max_scr = sum(nums)
        result = [0]
        
        for i, v in enumerate(nums, 1):
            scr += 1 if v == 0 else -1
            if scr > max_scr:
                result = [i]
                max_scr = scr
            elif scr == max_scr:
                result.append(i)
        
        return result
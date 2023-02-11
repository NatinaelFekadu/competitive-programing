class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        output = []
        
        for index in range(len(l)):
            temp = sorted(nums[l[index]:r[index]+1])
            
            diff = temp[1] - temp[0]
            is_found = False
            for index in range(2, len(temp)):
                if diff != temp[index] - temp[index-1]:
                    output.append(False)
                    is_found = True
                    break
            if not is_found:
                output.append(True)
        
        return output

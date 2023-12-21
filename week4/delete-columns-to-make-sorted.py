class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        columns_to_delete = 0
        for i in range(len(strs[0])):
            for j in range(len(strs)-1):
                if strs[j][i] > strs[j+1][i]:
                    columns_to_delete += 1
                    break
        return columns_to_delete
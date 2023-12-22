class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap = {}
        for r,row in enumerate(board):
            for i,val in enumerate(row):
                if val in hashmap:
                    for c in hashmap[val]:
                        if c[0] // 3 == r // 3 and c[1] // 3 == i // 3:
                            return False
                        elif (c[0] == r or c[1] == i):
                            return False
                    hashmap[val].append([r,i])
                if val != "." and val not in hashmap:
                    hashmap[val] = [[r,i]]
        return True
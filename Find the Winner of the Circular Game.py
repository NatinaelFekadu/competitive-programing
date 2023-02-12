class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ret=[]
        for index in range(1,n+1):
            ret.append(index)
        move=k-1
        while len(ret)!=1:
            ret.pop(move)
            move+=k-1
            move=move%len(ret)

        return ret[0]

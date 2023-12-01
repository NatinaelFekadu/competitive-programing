class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        alp = 'abcdefghijklmnopqrstuvwxyz'
        d = {}
        for i in range(26):
            d[order[i]] = alp[i]

        def fmt(st: str):
            normal = ''
            for i in st:
                normal += d[i]
            return normal

        for i in range(len(words)-1):
            if fmt(words[i]) > fmt(words[i+1]):
                return False

        return True
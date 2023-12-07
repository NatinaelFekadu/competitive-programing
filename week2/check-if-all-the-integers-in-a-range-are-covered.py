class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = {}
        for val in range(left,right + 1):
          covered[val] = False
        for val in range(left, right + 1):
          for r in ranges:
            if val in range(r[0],r[1]+1):
              covered[val] = True
        for key in covered:
          if not covered[key]:
            return False
        return True

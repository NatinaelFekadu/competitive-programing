class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        occurance = {s[i]: i for i in range(len(s))}
        i, ans = 0, []
        while i < len(s):
            end, j = occurance[s[i]], i + 1
            while j < end:
                if occurance[s[j]] > end:
                    end = occurance[s[j]]
                j += 1
           
            ans.append(end - i + 1)
            i = end + 1
            
        return ans
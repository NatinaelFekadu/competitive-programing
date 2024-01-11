class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        res = left = right = 0 
        ans={'T':0, 'F':0}
        while right < len(answerKey):
            while min(ans['T'], ans['F']) > k:
                ans[answerKey[left]] -= 1
                left += 1
            ans[answerKey[right]] += 1
            right += 1
            if min(ans['T'], ans['F']) <= k:
                res=max(res, right-left)
            
        return res
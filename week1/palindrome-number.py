class Solution:
    def isPalindrome(self, x: int) -> bool:
        curr_num = x
        temp = 0
        while x > 0:
            temp = (temp * 10) + (x % 10)
            x = x // 10
        return curr_num == temp
        
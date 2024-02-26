class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for index in range(len(s)):
            if s[index] != "]":
                stack.append(s[index])
            else:
                substring = ""
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num) * substring)
        return "".join(stack)
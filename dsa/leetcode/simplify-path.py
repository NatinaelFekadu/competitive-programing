class Solution:
    def simplifyPath(self, path: str) -> str:
        l=path.split('/')
        stack=[]
        print(l)
        for i in l:
            if i == '..'and len(stack) > 0:
                stack.pop()
            elif i != '.' and i != '' and i != '..':
                stack.append(i)
        
        return  '/'+'/'.join(stack)
        
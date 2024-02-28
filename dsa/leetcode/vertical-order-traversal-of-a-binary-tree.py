# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def inorder(root = root, values = [],row = 1, col = -1):
            if root:
                inorder(root.left,values,row+1,col-1)
                values.append([root.val,row-1,col+1])
                inorder(root.right,values,row+1, col+1)
            return values
        values = inorder()
        values.sort(key=lambda x:(x[2],x[1],x[0]))
        print(values)
        ans = []
        temp = []
        curr = values[0][2]
        for val,row,col in values:
            if col == curr:
                temp.append(val)
            else:
                curr = col
                ans.append(temp)
                temp = [val]
        ans.append(temp)
        return ans
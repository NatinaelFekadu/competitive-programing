# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def traverse(root = root,paths = [], num = 0):
            if not root:
                return
            num = (num* 10) + root.val
            traverse(root.left,paths,num)
            traverse(root.right,paths,num)
            if not root.left and not root.right:
                paths.append(num)
            return paths
        return sum(traverse())
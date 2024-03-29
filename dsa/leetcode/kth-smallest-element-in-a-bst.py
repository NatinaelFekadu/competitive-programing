# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def traverse(root = root, values = []):
            if not root:
                return
            traverse(root.left, values)
            values.append(root.val)
            traverse(root.right, values)
            return values
        return traverse()[k - 1]
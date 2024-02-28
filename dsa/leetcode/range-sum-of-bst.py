# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def get_value(root = root):
            if not root:
                return 0
            return root.val * (low <= root.val <= high) + get_value(root.left) + get_value(root.right)
        return get_value()
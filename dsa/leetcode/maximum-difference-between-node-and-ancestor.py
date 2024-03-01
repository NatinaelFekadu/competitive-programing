# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root = root, min_val = float("inf"), max_val = 0):
            if not root:
                nonlocal ans
                ans = max(ans, max_val - min_val)
                return
            dfs(root.left, min(min_val, root.val), max(max_val, root.val))
            dfs(root.right, min(min_val, root.val), max(max_val, root.val))
        dfs()
        return ans
            

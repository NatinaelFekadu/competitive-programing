class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def inorder(root):
            if root is None:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        nums = inorder(root)

        def bst(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            return TreeNode(nums[mid], bst(l, mid - 1), bst(mid + 1, r))

        return bst(0, len(nums) - 1)

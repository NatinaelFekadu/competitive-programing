# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root = root, values = []):
            if root:
                traverse(root.left,values)
                values.append(root.val)
                traverse(root.right, values)
            return values
        count = Counter(traverse())

        max_count = float("-inf")
        for val in count:
            if count[val] > max_count:
                max_count = count[val]
        res = []
        for val in count:
            if count[val] == max_count:
                res.append(val)
        return res
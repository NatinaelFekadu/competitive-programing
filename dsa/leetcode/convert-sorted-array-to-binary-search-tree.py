class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0: 
            return None
        mid  = len(nums) // 2
        root = TreeNode(val=nums[mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        root.left  = self.sortedArrayToBST(nums[:mid])
        return root
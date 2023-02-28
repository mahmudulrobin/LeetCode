class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root:
            if root.val == val:
                return root
            elif val > root.val:
                return self.searchBST(root.right, val)
            else:
                return self.searchBST(root.left, val)



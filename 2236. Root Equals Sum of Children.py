# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        self.ans=0
        self.ans+=root.left.val
        self.ans+=root.right.val
        if root.val == self.ans:
            return True
        else:
            return False

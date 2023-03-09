class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return None
        q = deque([root])
        res = []
        while q:
            node_each_level = []
            for i in range(len(q)):
                node = q.popleft()
                node_each_level.append(float(node.val))
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            avg = sum(node_each_level) / len(node_each_level)
            res.append(avg)
        return res

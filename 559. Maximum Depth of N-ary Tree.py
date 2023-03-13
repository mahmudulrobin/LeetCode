class Solution:
    def maxDepth(self, root: 'Node') -> int:
        q = deque()
        q.append((root,1))
        depth=0
        max=0
        while q:
            node,val = q.popleft()
            max = val
            if node.children:
                for nodes in node.children:
                    q.append((nodes, val+1))
        return max
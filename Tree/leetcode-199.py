# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            length = len(q)

            for i in range(length):
                v = q.popleft()
                if v.left:
                    q.append(v.left)
                if v.right:
                    q.append(v.right)

                if i == length - 1:
                    res.append(v.val)
            
        return res
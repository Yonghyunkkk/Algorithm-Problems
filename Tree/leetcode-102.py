from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if root:
            q = deque([root])
        else:
            return res

        while q:
            length = len(q)

            level = []

            for i in range(length):
                v = q.popleft()

                if v:
                    level.append(v.val)
                    if v.left:
                        q.append(v.left)
                    if v.right:
                        q.append(v.right)

            res.append(level)

        return res
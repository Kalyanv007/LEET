# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        if not root:
            return result
        flag=False
        q=deque([root])
        while q:
            level=[]
            size=len(q)
            for i in range(size):
                cur=q.popleft()
                level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                
            if flag:
                level.reverse()
            result.append(level)
            flag= not flag
        return result
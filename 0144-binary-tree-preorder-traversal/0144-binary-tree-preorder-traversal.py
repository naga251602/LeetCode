# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def postOrder(root):
            if root == None: return
            res.append(root.val)
            postOrder(root.left)
            postOrder(root.right)
        postOrder(root)
        return res
        
        
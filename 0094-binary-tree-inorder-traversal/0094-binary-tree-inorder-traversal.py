# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder_dfs(root):
            if root == None: return
            inorder_dfs(root.left)
            res.append(root.val)
            inorder_dfs(root.right)
        
        inorder_dfs(root)
        return res
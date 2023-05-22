# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True

        pre_val = pow(-2,31) -1
        cur = root
        stack = []
        while True:
            if cur is not None:
                stack.append(cur)
                cur = cur.left    
            elif stack:
                cur = stack.pop()
                if cur.val <= pre_val:
                    return False
                pre_val = cur.val
                cur = cur.right
            else:
                break
        return True
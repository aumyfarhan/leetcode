# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        self.balanced = True

        
    def get_height(self,root):
        
        if root:
            if (root.left):
                left_depth = self.get_height(root.left)

            else:
                left_depth=0

            if (root.right):
                right_depth = self.get_height(root.right)

            else:
                right_depth=0

            if abs(right_depth-left_depth)>1:
                self.balanced = False
            if (left_depth>=right_depth):
                depth = left_depth
            else:
                depth = right_depth

            return depth+1
    
    def isBalanced(self, root: TreeNode) -> bool:
        
        temp = self.get_height(root)
        
        return self.balanced
# Runtime: 5 ms
# Memory: 20.3 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        result = []
        self.smallest(root , result)
        return result[k-1]

    def smallest(self , root, result) :
        if root == None:
            return 
        self.smallest(root.left , result)
        result.append(root.val)
        self.smallest(root.right , result)

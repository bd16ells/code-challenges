# Add one Row to Tree
# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3666/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            new_root = TreeNode(val=v, left=root)
            return new_root
        else:
            noderef = []
            self.traverse(root, 1, d-1, noderef)
            for node in noderef:
                if node != None:
                    node.left = TreeNode(val=v, left=node.left)
                    node.right = TreeNode(val=v, right=node.right)
                
        return root
        
    def traverse(self, cur_node, cur_height, depth, noderef):
        
        if cur_height == depth:
            noderef.append(cur_node)
            return noderef
        if not cur_node:
            return noderef

        else:
            self.traverse(cur_node.left, cur_height+1, depth, noderef)
            self.traverse(cur_node.right, cur_height+1, depth, noderef)
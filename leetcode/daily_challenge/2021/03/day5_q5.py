# Average of Levels in Binary Tree
# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3661/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        arr = []
        if not root:
            return arr
        self.traverse(root, 1, arr)
        return [sum(level)/len(level) for level in arr]
        
    def traverse(self, cur_node, height, arr):
        if not cur_node: # end of path
            return
        if height > len(arr): # new level
            arr.append([cur_node.val])
        else: # already have visited this level
            arr[height-1].extend([cur_node.val])
        
        self.traverse(cur_node.left, height+1, arr)
        self.traverse(cur_node.right, height+1, arr)
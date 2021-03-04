# Intersection of Two Linked Lists
# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3660/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        setA = set()
        
        while(headA != None):
            setA.add(headA)
            headA = headA.next
            
        
        while(headB != None):
            if (headB in setA):
                return headB
            headB = headB.next
        return None
# Swap Nodes in Linked List
# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3671/
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        arr = []
        while head != None:
            arr.append(head.val)
            head = head.next
        temp = arr[k-1]
        arr[k-1] = arr[len(arr)-k]
        arr[len(arr)-k] = temp
        head = ListNode(arr[0])
        headPtr = head
        for i in range(1, len(arr)):
            headPtr.next = ListNode(arr[i])
            headPtr = headPtr.next
        return head
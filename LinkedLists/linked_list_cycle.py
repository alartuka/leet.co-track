## Link to the problem: https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        n = head
        while n and n.next:
            head = head.next # moves by 1 node
            n = n.next.next # moves by 2 nodes 
            if n is head: # pointers meet/point at the same node => a cycle
                return True
        return False
        

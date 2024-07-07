## Link to the problem: https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        n1 = ""
        n2 = ""

        # store each val of a linked list in a string
        c1 = l1
        while c1.next != None:
            n1 += str(c1.val)
            c1 = c1.next
        n1 += str(c1.val)

        c2 = l2
        while c2.next != None:
            n2 += str(c2.val)
            c2 = c2.next
        n2 += str(c2.val)

        # reverse the strings to represent the actual numbers
        n1 = n1[::-1]
        n2 = n2[::-1]

        r = int(n1) + int(n2)
        r = str(r)
        r = r[::-1]
        
        # store the sum result in a linked list
        n = ListNode(r[0])
        cur = n
        for c in r:
            cur.next = ListNode(c)
            cur = cur.next
        return n.next












        

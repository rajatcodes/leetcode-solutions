# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carryover = 0
        l3 = ListNode(0)
        current = l3
        while(l1!=None) or (l2!=None):
            if(l1==None):
                x1=0
            else:
                x1 = l1.val
            if(l2==None):
                x2=0
            else:
                x2 = l2.val
            x3 = int(x1)+int(x2)+int(carryover)
            carryover = x3 // 10
            x3 = x3 % 10
            current.val = x3
            if(l1!=None):
                l1 = l1.next
            if(l2!=None):
                l2=l2.next
            if(l1!=None) or (l2!=None):
                current.next = ListNode(0)
                current = current.next
        if(carryover!=0):
            current.next = ListNode(0)
            current = current.next
            current.val = carryover
        return l3
            

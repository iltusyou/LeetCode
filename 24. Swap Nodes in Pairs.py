# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def array_to_listnodes(arr):
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next

    return dummy.next

def print_nodes(nodes):
    while nodes:
        print(nodes.val, end=" -> ")
        nodes = nodes.next
    print("None")

class Solution:
    def getFirst2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode(head.val)
        if head.next:
            res.next = ListNode(head.next.val)        

        return res

    def swapSubPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head

        dummy = ListNode()                   
        tmp = head.next
        head.next = head.next.next
        tmp.next=head
        dummy.next = tmp
                                            
        return dummy.next
        
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        res = ListNode() 
        res_end = res
        
        while head and head.next:
            first2 = self.getFirst2(head)            
            tmp = self.swapSubPairs(first2)
            res_end.next = tmp
            res_end = res_end.next.next
            
            head=head.next.next

        if head:
            res_end.next = head
                                                        
        return res.next
        
        dummy = ListNode()                   
        tmp = head.next
        head.next = head.next.next
        tmp.next=head
        dummy.next = tmp
                                            
        return dummy.next
    
    




            



        
    
head = [1,2,3]
head_nodes = array_to_listnodes(head)
print_nodes(head_nodes)

s=Solution()
r = s.swapPairs(head_nodes)
print_nodes(r)

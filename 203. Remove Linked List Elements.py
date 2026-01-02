from typing import List, Optional

# Definition for singly-linked list.
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
            
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(next = head)    
        current = dummy_head

        while current.next: 
                               
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next            
            print(current.val)            
            
        return dummy_head.next



head = [1,2,6,3,4,5,6]
val = 6
# 1,2,3,4,5
head_node = array_to_listnodes(head)
print_nodes(head_node)


s = Solution()
cur = s.removeElements(head_node, val)
print_nodes(cur)





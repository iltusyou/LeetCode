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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:                        
        prev = None
        cur = head
        
        while cur:
            tmp = cur.next                    
            prev =  ListNode(cur.val, prev) 
            cur = tmp            
        return prev



arr = [1,2,3,4,5]
nodes = array_to_listnodes(arr)
print_nodes(nodes)


s = Solution()
r = s.reverseList(nodes)
print_nodes(r)
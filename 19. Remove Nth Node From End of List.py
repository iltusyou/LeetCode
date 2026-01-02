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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0,head)
        slow = dummy
        fast = dummy.next
        i = 0

        while i < n:
            # print(fast.val)
            fast = fast.next
            i += 1

        
        while fast:

            print(f"fast:{fast.val}, slow:{slow.val}")
            fast=fast.next
            slow=slow.next
                                
        slow.next = slow.next.next
        return dummy.next
        
    
# head = [1,2,3,4,5]
# n = 2

# head = [1]
# n = 1

head = [1,2]
n = 1

head_nodes = array_to_listnodes(head)
print_nodes(head_nodes)

s=Solution()
r = s.removeNthFromEnd(head_nodes, n)
print_nodes(r)

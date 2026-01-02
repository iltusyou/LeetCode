class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
        return



class MyLinkedList:

    def __init__(self):
        self.dummy = ListNode()        
        self.size = 0

    def get(self, index: int) -> int:                
        if index >= self.size or index < -1:
            return -1
        
        cur = self.dummy.next        
        for i in range(0, index):
            cur=cur.next

        return cur.val        

    def addAtHead(self, val: int) -> None:                
        self.dummy.next = ListNode(val, self.dummy.next)
        self.size += 1

    def addAtTail(self, val: int) -> None:        
        cur = self.dummy
        for i in range(0, self.size):
            cur = cur.next

        cur.next = ListNode(val)
        self.size += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if(index > self.size):
            return

        cur = self.dummy
        for i in range(0, index):
            cur = cur.next

        cur.next = ListNode(val, cur.next)
        self.size += 1             

    def deleteAtIndex(self, index: int) -> None:
        if(index >= self.size):
            return

        cur = self.dummy
        for i in range(0, index):
            cur = cur.next
        
        if cur.next:
            cur.next = cur.next.next        
        else:
            cur.next = None
        self.size -=1        
    
    def print(self):
        print(f"size:{self.size} ," , end=" ")

        cur = self.dummy.next
        while cur:
            print(cur.val, end=" -> ")
            cur = cur.next

        print("None")




# t1 = ["MyLinkedList","addAtHead","addAtTail","addAtTail","addAtTail","addAtTail","addAtTail","addAtTail","deleteAtIndex","addAtHead","addAtHead","get","addAtTail","addAtHead","get","addAtTail","addAtIndex","addAtTail","addAtHead","addAtHead","addAtHead","get","addAtIndex","addAtHead","get","addAtHead","deleteAtIndex","addAtHead","addAtTail","addAtTail","addAtIndex","addAtTail","addAtHead","get","addAtTail","deleteAtIndex","addAtIndex","deleteAtIndex","addAtHead","addAtTail","addAtHead","addAtHead","addAtTail","addAtTail","get","get","addAtHead","addAtTail","addAtTail","addAtTail","addAtIndex","get","addAtHead","addAtIndex","addAtHead","addAtTail","addAtTail","addAtIndex","deleteAtIndex","addAtIndex","addAtHead","addAtHead","deleteAtIndex","addAtTail","deleteAtIndex","addAtIndex","addAtTail","addAtHead","get","addAtIndex","addAtTail","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","deleteAtIndex","get","get","addAtHead","get","addAtTail","addAtTail","addAtIndex","addAtIndex","addAtHead","addAtTail","addAtTail","get","addAtIndex","addAtHead","deleteAtIndex","addAtTail","get","addAtHead","get","addAtHead","deleteAtIndex","get","addAtTail","addAtTail"]
# t2 = [[],[38],[66],[61],[76],[26],[37],[8],[5],[4],[45],[4],[85],[37],[5],[93],[10,23],[21],[52],[15],[47],[12],[6,24],[64],[4],[31],[6],[40],[17],[15],[19,2],[11],[86],[17],[55],[15],[14,95],[22],[66],[95],[8],[47],[23],[39],[30],[27],[0],[99],[45],[4],[9,11],[6],[81],[18,32],[20],[13],[42],[37,91],[36],[10,37],[96],[57],[20],[89],[18],[41,5],[23],[75],[7],[25,51],[48],[46],[29],[85],[82],[6],[38],[14],[1],[12],[42],[42],[83],[13],[14,20],[17,34],[36],[58],[2],[38],[33,59],[37],[15],[64],[56],[0],[40],[92],[63],[35],[62],[32]]

t1 = ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
t2 = [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]

obj = MyLinkedList()


max = len(t1)

for i in range(1, max):    
    print(f"{i}: {t1[i]} {t2[i]}", end=" ")
    match t1[i]:
        case "addAtHead":            
            obj.addAtHead(t2[i][0])
            obj.print()
                               
        case "addAtTail":            
            obj.addAtTail(t2[i][0])
            obj.print()
                       
        case "addAtIndex":            
            obj.addAtIndex(t2[i][0], t2[i][1])
            obj.print()
                          
        case "get":            
            print(obj.get(t2[i][0]))            
                  
        case "deleteAtIndex":            
            obj.deleteAtIndex(t2[i][0])
            obj.print()

    # if(t1[i] == "deleteAtIndex"):
    #     break
    

# print(t1[58],t2[57][0], t2[57][1])
                              

# obj.print()
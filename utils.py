"""
LeetCode 工具函數
包含常用的資料結構和轉換函數
"""

from typing import Optional, List
from collections import deque


# ==================== 二叉樹節點定義 ====================

class TreeNode:
    """二叉樹節點"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode({self.val})"


# ==================== Array ↔ TreeNode 轉換 ====================

def arrayToTree(arr: List[Optional[int]]) -> Optional[TreeNode]:
    """
    將 LeetCode 格式的 array 轉換成二叉樹
    
    參數:
        arr: 例如 [1,2,3,null,null,4,5]
    
    返回:
        TreeNode 根節點，空樹返回 None
    
    範例:
        >>> root = arrayToTree([1, 2, 3])
        >>> root.val
        1
        >>> root.left.val
        2
    """
    if not arr or arr[0] is None:
        return None
    
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(arr):
        node = queue.popleft()
        
        # 處理左子節點
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        
        # 處理右子節點
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    
    return root

def treeToArray(root: Optional[TreeNode]) -> List[Optional[int]]:
    """
    將二叉樹轉換回 LeetCode 格式的 array
    
    參數:
        root: TreeNode 根節點
    
    返回:
        List[Optional[int]]
    
    範例:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> treeToArray(root)
        [1, 2, 3]
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # 移除尾部的 None
    while result and result[-1] is None:
        result.pop()
    
    return result


# ==================== 打印樹結構 ====================

def printTree(root: Optional[TreeNode], level=0, prefix="Root: "):
    """
    以樹狀結構打印二叉樹（方便調試）
    
    參數:
        root: TreeNode 根節點
        level: 當前層級（內部使用）
        prefix: 前綴字符（內部使用）
    
    範例:
        >>> root = arrayToTree([1, 2, 3, 4, 5])
        >>> printTree(root)
        Root: 1
            L--- 2
                L--- 4
                R--- 5
            R--- 3
    """
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left or root.right:
            if root.left:
                printTree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                printTree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")


# ==================== 鏈表節點定義 ====================

class ListNode:
    """單向鏈表節點"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"ListNode({self.val})"


def arrayToList(arr: List[int]) -> Optional[ListNode]:
    """
    將 array 轉換成鏈表
    
    參數:
        arr: 例如 [1, 2, 3, 4]
    
    返回:
        ListNode 頭節點
    
    範例:
        >>> head = arrayToList([1, 2, 3])
        >>> head.val
        1
        >>> head.next.val
        2
    """
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head


def listToArray(head: Optional[ListNode]) -> List[int]:
    """
    將鏈表轉換回 array
    
    參數:
        head: ListNode 頭節點
    
    返回:
        List[int]
    
    範例:
        >>> head = ListNode(1, ListNode(2, ListNode(3)))
        >>> listToArray(head)
        [1, 2, 3]
    """
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result


def printList(head: Optional[ListNode]):
    """
    打印鏈表（方便調試）
    
    範例:
        >>> head = arrayToList([1, 2, 3, 4])
        >>> printList(head)
        1 -> 2 -> 3 -> 4 -> None
    """
    values = listToArray(head)
    print(" -> ".join(map(str, values)) + " -> None")
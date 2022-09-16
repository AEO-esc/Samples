from lib2to3.pytree import Node
from typing import List

# Linked list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# handle list operations
class LinkkedList:
    def __init__(self):
        self.head = None
    def reverseList(self, head):
        if head is None or head.next is None:
            return head;
        rest = self.reverseList(ne)

class Solution():
    def reverseList(self, head: ListNode) -> ListNode:
        previousNode = None
        currentNode = head
        while currentNode:
            nextNode = currentNode
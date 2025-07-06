# Last updated: 7/5/2025, 11:02:48 PM
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        node = self.head.next
        for _ in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.size:
            node = self.head
            for _ in range(index):
                node = node.next
            nxt = node.next
            node.next = ListNode(val, nxt)
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < self.size:
            node = self.head
            for _ in range(index):
                node = node.next
            node.next = node.next.next
            self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
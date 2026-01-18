class Node(object):
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index):
        cur = self.head.next
        while cur != self.tail:
            if index == 0:
                return cur.val
            index -= 1
            cur = cur.next
        return -1
        
    def addAtHead(self, val):
        cur = Node(val)
        cur.next = self.head.next
        cur.prev = self.head 
        self.head.next.prev = cur 
        self.head.next = cur

    def addAtTail(self, val):
        self.addBeforeNode(self.tail, val)

    def addBeforeNode(self, node, val):
        cur = Node(val)
        cur.next = node
        cur.prev = node.prev 
        node.prev.next = cur 
        node.prev = cur


    def addAtIndex(self, index, val):
        cur = self.head.next
        while index > 0 and cur != self.tail:
            cur = cur.next
            index -= 1
        if index == 0:
            self.addBeforeNode(cur, val)
        

    def deleteAtIndex(self, index):
        cur = self.head.next
        while index > 0 and cur != self.tail:
            cur = cur.next
            index -= 1
        if index == 0 and cur != self.tail:
            cur.next.prev = cur.prev
            cur.prev.next = cur.next


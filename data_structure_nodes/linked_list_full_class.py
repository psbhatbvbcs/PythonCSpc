class LinkedListNode:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def insert(self, value):
        node = LinkedListNode(value)
        if self.head is None:
            self.head = node
            return
        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode

    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value + '->')
            currentNode = currentNode.nextNode
        else:
            print(None)


ll = LinkedList()
ll.printLinkedList()
ll.insert('3')
ll.printLinkedList()
ll.insert('44')
ll.printLinkedList()

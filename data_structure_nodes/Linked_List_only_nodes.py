class LinkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


# 3 -> 7 -> 10

node1 = LinkedListNode('3')  # '3'
node2 = LinkedListNode('7')  # '7'
node3 = LinkedListNode('10')  # '10'

node1.nextNode = node2
node2.nextNode = node3

currentNode = node1
while True:
    print(currentNode.value, '->')
    if currentNode.nextNode is None:
        print('None')
        break
    currentNode = currentNode.nextNode

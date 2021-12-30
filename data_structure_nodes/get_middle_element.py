class LinkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


def getMiddleElement(head):
    fastRunner = head
    slowRunner = head
    tick = False
    while fastRunner:
        fastRunner = fastRunner.nextNode
        if tick == True:
            slowRunner = slowRunner.nextNode
        tick = not tick
    return slowRunner.value

node1 = LinkedListNode('3')
node2 = LinkedListNode('7')
node3 = LinkedListNode('10')
node4 = LinkedListNode('12')


node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4


print(getMiddleElement(node1))

class Node(object):
    
    def __init__(self, value):
        self.value = value
        self.next_node = None
        
    def printList(self, a):
        current = a
        while current:
            print current.value
            current = current.next_node
        
a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c

a.printList(a)
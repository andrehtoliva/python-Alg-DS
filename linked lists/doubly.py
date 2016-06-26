class Node(object):
    
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None
        
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next_node = b
b.next_node = c
c.next_node = d

b.prev_node = a
c.prev_node = b
d.prev_node = c
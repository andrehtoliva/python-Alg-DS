class Node(object):
    
    def __init__(self,value):
        self.value = value
        self.next_node = None

def cycle_check(node):
    
    marker1 = node
    marker2 = node
    
    while marker2 != None and marker2.next_node != None:
        marker1 = marker1.next_node
        marker2 = marker2.next_node.next_node
        
        if marker2 == marker1:
            return True
        
    return False

a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c
c.next_node = a # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.next_node = y
y.next_node = z

print cycle_check(a)
print cycle_check(x)
    
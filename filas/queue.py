class Queue(object):
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
        
    def enqueue(self, item):
        self.items.insert(0,item)
        
    def pop(self):
        return self.items.pop()
        
    def size(self):
        return len(self.items)
        
fila = Queue()
print fila.isEmpty()
fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)
print fila.isEmpty()
print fila.pop()
print fila.size()
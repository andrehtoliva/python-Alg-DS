class Deque(object):
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
        
    def front(self,items):
        self.items.append(items)
        
    def rear(self,items):
        self.items.insert(0,items)
        
    def popfront(self):
        return self.items.pop()
        
    def poprear(self):
        return self.items.pop(0)
        
    def size(self):
        return len(self.items)
        

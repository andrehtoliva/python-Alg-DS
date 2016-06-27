class BinaryTree(object):
    
    def __init__(self,rootObj):
        
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
        
    def insertLeft(self,newNode):
        
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
        
        
    def insertRight(self,newNode):
        
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
            
    def getRightChild(self):
        return self.rightChild
        
    def getLeftChild(self):
        return self.leftChild
        
    def setRootVal(self,obj):
        self.key = obj
        
    def getRootVal(self):
        return self.key
        
tree_vals = []        

def inorder(tree):
    
    if tree != None:
        inorder(tree.getLeftChild())
        tree_vals.append(tree.getRootVal())
        inorder(tree.getRightChild())
        
def validateBST(tree_vals):
    return tree_vals == sorted(tree_vals)
    
        
        
        
r = BinaryTree(5)
r.insertLeft(4)
r.insertLeft(3)
r.insertRight(6)
r.insertRight(7)

inorder(r)
print validateBST(tree_vals)


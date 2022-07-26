class BinaryTree :
    def __init__(self, root):
        self.root = root
    
    def addNode(self, leaf):
        if(type(leaf) != Leaf):
            return False
        
        currLeaf = self.root
        while bool(currLeaf.previous) or bool(currLeaf.next) :
            if currLeaf.value > leaf.value :
                currLeaf = currLeaf.previous
            else :
                currLeaf = currLeaf.next 
        
    def print(self):
        print({'root':self.root.value, 'previous' : self.root.previous, 'next': self.root.next})
        
class Leaf:
    def __init__(self, value):
        self.value = value
        self.previous = False
        self.next = False
    
    def print(self):
        print({'value' : self.value, 'previous' : self.previous, 'next' : self.next}) 
        

leaf1 = Leaf(10)

tree = BinaryTree(leaf1)

leaf1.print()
tree.print()
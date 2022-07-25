class BinaryTree :
    def __init__(self, root):
        self.root = root
    
    def addNode(self, node):
        if(type(node) != Node):
            return False
        
        currNode = self.root
        while bool(currNode.previous) or bool(currNode.next) :
            if currNode.value > node.value :
                currNode = currNode.previous
            else :
                currNode = currNode.next 
        
        
                
        
    def print(self):
        print({'root':self.root.value, 'previous' : self.root.previous, 'next': self.root.next})
        
        
        


class Node:
    def __init__(self, value):
        self.value = value
        self.previous = False
        self.next = False
    
    def print(self):
        print({'value' : self.value, 'previous' : self.previous, 'next' : self.next}) 
        

node1 = Node(10)

tree = BinaryTree(node1)

node1.print()
tree.print()
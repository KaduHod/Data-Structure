import random
import string

from files.createJsonFile import writeJsonTree
    
class BinaryTree :
    def __init__(self, root):
        self.root = root
    
    def addChild(self, child):
        if(type(child) != Child):
            return False
        currChild = self.root
        while bool(currChild.left) or bool(currChild.right) :
            if child.value > currChild.value :
                if bool(currChild.right) :
                    currChild = currChild.right
                else :
                    break
            else :
                if bool(currChild.left) : 
                    currChild = currChild.left
                else :
                    break
        if(child.value == currChild.value) :
            return False
        if child.value > currChild.value :
            currChild.right = child
        else :
            currChild.left = child
                
    def print(self):
        print({'root':self.root.value, 'left' : self.root.left.value, 'right': self.root.right.value})
        
    def visitChild(self,leaf):
        if(leaf.left != False):
            writeJsonTree(leaf.left, leaf, 'left')
            self.visitChild(leaf.left)
        if(leaf.right != False) :
            writeJsonTree(leaf.right, leaf, 'right')
            self.visitChild(leaf.right)
        if(leaf.left == False and leaf.right == False): 
            writeJsonTree(leaf.right, leaf, 'last')
        
class Child:
    def __init__(self, value):
        self.value = value
        self.left  = False
        self.right = False
    
    def print(self):
        print({'value' : self.value, 'left' : self.left.value if bool(self.left) else self.left, 'right' : self.right.value if bool(self.right) else self.right}) 
        
   







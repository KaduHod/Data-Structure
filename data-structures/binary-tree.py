        
def setId():
    import random
    import string
    
    letters = string.ascii_lowercase
    randomId = ''.join(random.choice(letters) for i in range(20))
    return randomId

class BinaryTree :
    def __init__(self, root):
        self.root = root
    
    def addChild(self, child):
        
        if(type(child) != Child):
            return False
        currChild = self.root
        while bool(currChild.left) or bool(currChild.right) :
            if child.value > currChild.value : # Se maior e tiver valor, ir para direita
                if bool(currChild.right) :
                    currChild = currChild.right
                else :
                    break
            else :
                if bool(currChild.left) : # Se menor e tiver valor, ir para esquerda
                    currChild = currChild.left
                else :
                    break
        if child.value > currChild.value :
            currChild.right = child
        else :
            currChild.left = child
                
    def print(self):
        print({'root':self.root.value, 'left' : self.root.left.value, 'right': self.root.right.value})
        
    def through(self):
        return True
        
class Child:
    def __init__(self, value):
        self.value = value
        self.left  = False
        self.right = False
    
    def print(self):
        print({'value' : self.value, 'left' : self.left.value if bool(self.left) else self.left, 'right' : self.right.value if bool(self.right) else self.right}) 

child1  = Child(50)
child2  = Child(55)
child3  = Child(40)
child4  = Child(70)
child5  = Child(30)
child6  = Child(35)
child7  = Child(45)
child8  = Child(80)
child9  = Child(60)
child10 = Child(69)

tree = BinaryTree(child1)
tree.addChild(child2)
tree.addChild(child3)
tree.addChild(child4)
tree.addChild(child5)
tree.addChild(child6)
tree.addChild(child7)
tree.addChild(child8)
tree.addChild(child9)
tree.addChild(child10)

# tree.print() # 50
# tree.root.right.print() #55
# tree.root.right.right.print() #70
# tree.root.right.right.left.print()#60
# tree.root.right.right.left.right.print()#69
# tree.root.right.right.right.print()#80
# 
# 
# tree.root.left.print() # 40
# tree.root.left.right.print() #45
# tree.root.left.left.print() #30
# tree.root.left.left.right.print() #30




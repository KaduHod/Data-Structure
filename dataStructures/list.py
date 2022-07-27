class LinkedList :
    def __init__(self, node):
        self.node = node
           
    def print(self):
        self.node.print()
        
    def addNode(self, node):
        if (type(node) != Node):
            return False
        
        currNode = self.node
        while currNode.pointer != False : 
            currNode = currNode.pointer
        currNode.pointer = node
    
    def removeNode(self, node):
        if (type(node) != Node):
            return False
        
        currNode = self.node
        while currNode.pointer != node and currNode.pointer != False :
            currNode = currNode.pointer
            
        if currNode.pointer.pointer != False:
            currNode.pointer = currNode.pointer.pointer
        else :
            currNode.pointer = False
            
    def getByIndex(self, index):
        if(type(index) != int or index < 1):
            return False
        
        cont = 1
        currNode = self.node
        while currNode.pointer != False and cont != index:
            currNode = currNode.pointer
            cont = cont+1
            
        return currNode
                
    def printList(self):
        currNode = self.node
        while currNode != False :
            currNode.print()
            currNode = currNode.pointer
            
        
        
class Node :
    value = False
    pointer = False
    def __init__(self, value):
        self.value = value
        self.pointer = False
        
    def print(self):
        if(bool(self.pointer)):
            print({'value': self.value, 'pointer': self.pointer.value})
        else :
            print({'value': self.value, 'pointer': self.pointer})

listNodes = [Node(1)]
lista = LinkedList(listNodes[0])

for current in range(2,100):
    no = Node(current)
    listNodes.append(no)
    lista.addNode(no)
    
node = lista.getByIndex(1)
if (bool(node)):
    node.print()
else:
    print(node)























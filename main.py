import math
import fibonacci
import json
from dataStructures.binaryTree import Child, BinaryTree


# CRIAR REPRESENTAÇÃO EM JSON DE UMA ARVORE BINARIA EM PYTHON

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
tree.root.print()
tree.visitChild(tree.root)

# jsonFile = open('files/json-padrao.json')
# jsonFileDecoded = json.load(jsonFile)
# print(jsonFileDecoded)



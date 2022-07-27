import json
from turtle import right

def writeJsonTree(jsonData, dad, way):
    if(bool(jsonData)):
        path = 'files/Json-padrao.json'
        data = {
            "data" : {
                "value" : jsonData.value,
                "left" :  jsonData.left.value if bool(jsonData.left) else False,
                "right" : jsonData.right.value if bool(jsonData.right) else False
            },
            'dad': dad.value,
            'way' : way
        }
        
        json = getJsonDataFromFile(path)
        writeJsonToFile(path, data, json)
    
    
def getJsonDataFromFile(path) :
    file = open(path)
    return json.load(file)

def writeJsonToFile(path, newChildData, tree) :
    newDictionary = insertChild(tree, newChildData["dad"], newChildData["data"]["value"], newChildData["way"])
    jsonFile = open(path, "w")
    newJsonTree = json.dumps(newDictionary)
    jsonFile.write(newJsonTree)
    jsonFile.close()
    
    
    
    

def insertChild(tree, searchValue, valueToInsert, side) :
    currChild = tree 
    
    if(currChild == {}) :
        tree = {"value":valueToInsert, "right" : False, "left" : False}
        return tree
    #acho o valor pai     
    while currChild["value"] != searchValue:
        if(bool(currChild) == False):
            return False
        if(searchValue > currChild["value"]) :
            currChild = currChild["right"]
        else :
            currChild = currChild["left"]
            
    currChild[side] = {"value":valueToInsert, "right" : False, "left" : False}
    return tree
    

    
    
    
    
  
import json

def createFile(name,extension) :
    with open(name +'.'+ extension, 'w') as f:
        print("The json file is created")
        
def getContentFromFile(path) :
    with open(path) as f:
        data = json.load(f)
        return data
        
# createFile('Json-padrao','json')
jsonVar = getContentFromFile('Json-padrao.json') 
print(jsonVar)
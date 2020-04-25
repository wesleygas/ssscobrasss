#Baseado no trabalho publicado por radk0s em https://github.com/radk0s/ply

class IdentSymbol():
    def __init__(self, name, value):
        self.name = name
        self.value = value

class FuncSymbol():
    def __init__(self, name, argList, block):
        self.name = name
        self.argList = argList
        self.block = block
        
class SymbolTable():
    def __init__(self, name=None, parent=None):
        self.symbols = {}
        self.name = name
        self.parent = parent
    
    def setSymbol(self, symbol):
        self.symbols[symbol.name] = symbol

    def getSymbol(self, name):
        if(name in self.symbols):
            return self.symbols[name]
        elif self.parent:
            return self.parent.getSymbol(name)
        else:
            raise Exception(f"'{name}' is not defined")
    
    def getParentScope(self):
        return self.parent
    
from symboltable import IdentSymbol, FuncSymbol, SymbolTable

class Number():
    def __init__(self, value):
        self.value = value
    def eval(self, st):
        return int(self.value)

class Block():
    def __init__(self):
        self.childs = []
    def eval(self, st):
        for child in self.childs:
            child.eval(st)

class Ident():
    def __init__(self, name):
        self.name = name
    def eval(self, st):
        return st.getSymbol(self.name).value

class FuncDef():
    def __init__(self, name, argList, block):
        self.name = name
        self.argList = argList
        self.block = block
    def eval(self, st):
        func = FuncSymbol(self.name, self.argList, self.block)
        st.setSymbol(func)

class FuncCall():
    def __init__(self, name, argList):
        self.name = name
        self.argList = argList
    def eval(self, st):
        func = st.getSymbol(self.name) #get function definition
        if(len(self.argList) != len(func.argList)): #check if has same arglen
            raise Exception(f"{self.name} receives {len(self.argList)} arguments but {func.argList} were given")
        
        funcSt = SymbolTable(self.name, st) #create local scope

        for i in range(len(func.argList)):  #copy args for local scope
            #                   Arg name       , arg value
            symb = IdentSymbol(func.argList[i],self.argList[i].eval())
            funcSt.setSymbol(symb)

        func.block.eval(funcSt) #run funcblock with local scope

class WhileNode():
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block
    def eval(self,st):
        while(self.condition.eval(st)):
            self.block.eval(st)

class IfNode():
    def __init__(self, condition, block_true, block_false = None):
        self.condition = condition
        self.block_true = block_true
        self.block_false = block_false
    def eval(self,st):
        if(self.condition.eval(st)):
            self.block_true.eval(st)
        elif(self.block_false):
            self.block_false.eval(st)
        

class UnOp():
    def __init__(self, child):
        self.child = child

class BinOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right


#Binops

class Sum(BinOp):
    def eval(self,st):
        return int(self.left.eval(st) + self.right.eval(st))

class Sub(BinOp):
    def eval(self,st):
        return int(self.left.eval(st) - self.right.eval(st))

class Div(BinOp):
    def eval(self,st):
        return int(self.left.eval(st) // self.right.eval(st))

class Mult(BinOp):
    def eval(self,st):
        return int(self.left.eval(st) * self.right.eval(st))

class Pow(BinOp):
    def eval(self,st):
        return int(self.left.eval(st) ** self.right.eval(st))

class Equal(BinOp):
    def eval(self,st):
        return int(self.left.eval(st) == self.right.eval(st))

class Greater(BinOp):
    def eval(self,st):
        return int(self.left.eval(st) > self.right.eval(st))

class Less(BinOp):
    def eval(self,st):
        return int(self.left.eval(st) < self.right.eval(st))

class Assign(BinOp):
    def eval(self, st):
        symbol = IdentSymbol(self.left.name, self.right.eval(st))
        st.setSymbol(symbol)



#UNOP 

class Print(UnOp):
    def eval(self, st):
        print(self.child.eval(st))

class Negate(UnOp):
    def eval(self,st):
        return -int(self.child.eval(st))

class Positive(UnOp):
    def eval(self,st):
        return +int(self.child.eval(st))


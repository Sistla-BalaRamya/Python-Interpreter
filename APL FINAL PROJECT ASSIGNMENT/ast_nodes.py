# Abstract Syntax Tree (AST) Nodes

class AssignNode:
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value

    def __repr__(self):
       return f"AssignNode(var = {self.variable}, expr = {self.value})"

class PrintNode:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"PrintNode(expr = {self.value})"

class BinOpNode:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"BinOpNode(left = {self.left}, operation = {self.operator}, right = {self.right})"

class NumberNode:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"NumberNode(value = {self.value})"

class VarNode:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"VarNode(name = {self.name})"
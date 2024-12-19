from ast_nodes import *

# Interpreter: Executes the AST
class Interpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, node):
            if isinstance(node, AssignNode):
                self.variables[node.variable] = self.interpret(node.value)
            elif isinstance(node, PrintNode):
                print(self.interpret(node.value))
            elif isinstance(node, BinOpNode):
                left = self.interpret(node.left)
                right = self.interpret(node.right)
                if node.operator == "+":
                    return left + right
                elif node.operator == "-":
                    return left - right
                elif node.operator == "*":
                    return left * right
                elif node.operator == "/":
                    return left / right
            elif isinstance(node, NumberNode):
                return node.value
            elif isinstance(node, VarNode):
                return self.variables.get(node.name, 0) 
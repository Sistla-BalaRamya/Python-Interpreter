from lexer import TokenType
from ast_nodes import *

# Parser: Converts tokens into an AST
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def parse(self):
        if self.peek().type == TokenType.KEYWORD:
            keyword = self.consume().value
            if keyword == "let":
                return self.parse_assignment()
            elif keyword == "print":
                return self.parse_print()
        else:
            raise ValueError("Unknown statement")

    def parse_assignment(self):
        variable = self.consume().value
        self.expect(TokenType.ASSIGN)
        value = self.parse_expression()
        self.expect(TokenType.SEMICOLON)
        return AssignNode(variable, value)

    def parse_print(self):
        value = self.parse_expression()
        self.expect(TokenType.SEMICOLON)
        return PrintNode(value)

    def parse_expression(self):
        left = self.parse_term()
        while self.peek() and self.peek().value in "+-":
            operator = self.consume().value
            right = self.parse_term()
            left = BinOpNode(left, operator, right)
        return left

    def parse_term(self):
        left = self.parse_factor()
        while self.peek() and self.peek().value in "*/":
            operator = self.consume().value
            right = self.parse_factor()
            left = BinOpNode(left, operator, right)
        return left

    def parse_factor(self):
        token = self.consume()
        if token.type == TokenType.NUMBER:
            return NumberNode(token.value)
        elif token.type == TokenType.IDENTIFIER:
            return VarNode(token.value)
        elif token.type == TokenType.PARENTHESIS and token.value == "(":
            expr = self.parse_expression()
            self.expect(TokenType.PARENTHESIS, ")")
            return expr
        else:
            raise ValueError("Invalid factor")

    def consume(self):
        token = self.tokens[self.position]
        self.position += 1
        return token

    def peek(self):
        return self.tokens[self.position] if self.position < len(self.tokens) else None

    def expect(self, token_type, value=None):
        token = self.consume()
        if token.type != token_type or (value and token.value != value):
            raise ValueError(f"Expected {token_type} {value}, got {token}")

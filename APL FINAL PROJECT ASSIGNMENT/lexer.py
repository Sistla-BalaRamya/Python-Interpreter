# Token Types
class TokenType:
    KEYWORD = "KEYWORD"
    IDENTIFIER = "IDENTIFIER"
    ASSIGN = "ASSIGN"
    NUMBER = "NUMBER"
    OPERATOR = "OPERATOR"
    SEMICOLON = "SEMICOLON"
    PARENTHESIS = "PARENTHESIS"

# Token Representation
class Token:
    def __init__(self, token_type, value=None):
        self.type = token_type
        self.value = value

    def printTokens(self):
        return f"Token (type = {self.type}, value = {self.value})"

# Lexer: Converts input string into tokens
class Lexer:
    OPERATORS = "+-*/"
    KEYWORDS = {"let", "print"}

    def tokenize(self, input_text):
        tokens = []
        i = 0

        while i < len(input_text):
            char = input_text[i]

            # Skip spaces
            if char.isspace():
                i += 1
                continue

            # Keywords or Identifiers
            if char.isalpha():
                start = i
                while i < len(input_text) and input_text[i].isalnum():
                    i += 1
                word = input_text[start:i]
                if word in self.KEYWORDS:
                    token_type = TokenType.KEYWORD
                else:
                    token_type = TokenType.IDENTIFIER
                tokens.append(Token(token_type, word))

            # Numbers
            elif char.isdigit():
                start = i
                while i < len(input_text) and input_text[i].isdigit():
                    i += 1
                tokens.append(Token(TokenType.NUMBER, int(input_text[start:i])))

            # Operators
            elif char in self.OPERATORS:
                tokens.append(Token(TokenType.OPERATOR, char))
                i += 1

            # Assignment
            elif char == "=":
                tokens.append(Token(TokenType.ASSIGN, char))
                i += 1

            # Semicolon
            elif char == ";":
                tokens.append(Token(TokenType.SEMICOLON, char))
                i += 1

            # Parentheses
            elif char in "()":
                tokens.append(Token(TokenType.PARENTHESIS, char))
                i += 1

            else:
                raise ValueError(f"Unknown character: {char}")

        return tokens

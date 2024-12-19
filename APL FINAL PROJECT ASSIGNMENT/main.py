from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def main():
    # Example Input
    input_code = """
    let x = 2 + 3;
    let y = 1 / 4; 
    print(x);
    print(y);
    print(x*y);
    """
    # Tokenization
    lexer = Lexer()
    tokens = lexer.tokenize(input_code)
    print("List of tokens generated from lexer:")
    for token in tokens:
        print(token.printTokens())
    
    # Parsing
    parser = Parser(tokens)
    interpreter = Interpreter()
    print("\nNodes from AST:")

    while parser.position < len(tokens):
        ast = parser.parse()
        print(ast)
        # Interpretation
        interpreter.interpret(ast)

    

if __name__ == "__main__":
    main()

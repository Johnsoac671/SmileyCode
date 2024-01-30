from nodes import FunctionDef, Literal, OperatorNode, UnaryOperatorNode, NameNode
from tokenizer import Tokenizer
    
class Parser:
    def __init__(self):
        self.stack = []
        
    def parse(self, tokenizer: Tokenizer):
        token = next(tokenizer)
        
        match token.type:
            
            case "STRUCTURE":
                
                if token.value == "📝":
                    self.stack += token.value
            
            case "TYPE":
                if token.value == "⚙️":
                    if self.stack[-1] == "📝":
                        self.stack.pop()
                        
                        func_name = next(tokenizer)
                        
from nodes import FunctionDef, Literal, OperatorNode, UnaryOperatorNode, CallNode
from tokenizer import Tokenizer, Token
    
class Parser:
    def __init__(self):
        self.stack = []
        
    def parse(self, tokenizer: Tokenizer):
        token = next(tokenizer)
        
        match token.type:
            
            case "STRUCTURE":
                self.parse_structure(token, tokenizer)
            
            case "TYPE":
                pass
                
    def parse_structure(self, token: Token, tokenizer: Tokenizer):
        
        match token.value:
            
            case "📝":
                declaration_type = next(tokenizer)
                
                if declaration_type == "⚙️":
                    self.define_func(tokenizer)
                else:
                    types = {}
                
            case "⏮️":
                body = self.stack.pop()
                func: FunctionDef = self.stack.pop()
                func.body = body
                
                        
    def define_func(self, tokenizer: Tokenizer):
                        
        func = FunctionDef()
            
        func.name = next(tokenizer)
        
        current_token = next(tokenizer).value
        self.check_token("⏩", current_token)
        
        while current_token != "⏪":
            if current_token != "⏩":
                func.args += current_token
                
            current_token = next(tokenizer).value
            
        current_token = next(tokenizer).value
        self.check_token("🟰", current_token)
        
        current_token = next(tokenizer).value
        self.check_token("⏭️", current_token)
        
        self.stack += func
        
                        
    def check_token(self, expected, token):
        
        if token != expected:
            raise SyntaxError(f"{expected} expected")
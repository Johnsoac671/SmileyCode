from nodes import FunctionDef, Literal, OperatorNode, UnaryOperatorNode, CallNode, AssignNode
from tokenizer import Tokenizer, Token
    
class Parser:
    def __init__(self):
        self.stack = Stack
        
    def parse(self, tokenizer: Tokenizer):
        token = next(tokenizer)
        
        match token.type:
            
            case "STRUCTURE":
                self.parse_structure(token, tokenizer)
            
            case "TYPE":
                pass

class Stack:
    
    def __init__(self):
        self.stack = [[]]
    
    def append(self, value):
        self.stack[-1].append(value)
    
    def pop_stack(self):
        return self.stack.pop()
    
    def pop(self):
        return self.stack[-1].pop()
        
                
    def parse_structure(self, token: Token, tokenizer: Tokenizer):
        match token.value:
            
            case "📝":
                declaration_type = next(tokenizer)
                
                if declaration_type == "⚙️":
                    self.define_func(tokenizer)
                else:
                    
                    types = {
                        "🧵" : str,
                        "🧮" : int,
                        "🎳" : float,
                        "👻" : bool
                    }
                    
                    name = next(tokenizer).value
                    next(tokenizer)
                    value = next(tokenizer).value
    
                    node = AssignNode(name, value, types[declaration_type.value])
                    self.stack.append(node)
                
            case "⏮️":
                body = self.stack.pop_stack()
                func = self.stack.pop()
                func.body = body
                self.stack.append(func)
                
                
            case "🙂":
                programFunc = FunctionDef()
                programFunc.name = "main"
                
                self.stack.append(programFunc)
                
                        
    def define_func(self, tokenizer: Tokenizer):
                        
        func = FunctionDef()
            
        func.name = next(tokenizer).value
        
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
        
        self.stack.append(func)
        
                        
    def check_token(self, expected, token):
        
        if token != expected:
            raise SyntaxError(f"{expected} expected")
        
if __name__ == "__main__":
    test = Tokenizer(r"🙂 📝 🧵 bob 🟰 \"Bob\" 🚫 😴")

    test2 = Parser()
    try:
        while True:
            test2.parse(test)
    except:
        print(test2.stack[0].name)
        print(test2.stack[0].body[0].name)
        print(test2.stack[0].body[0].value)
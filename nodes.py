class LeafNode:
    def __init__(self, value):
        self.value = value
  
        
class Node:
    def __init__(self, value, left, right):
        self.value = value
        
        self.left = left
        self.right = right


class OperatorNode(Node):
    
    def __init__(self, op, left, right):
        Node.__init__(op, left, right)
    
    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        
        match self.value:
            
            case "+":
                return left + right
            
            case "-":
                return left - right
            
            case "*":
                return left * right
            
            case "/":
                return left / right
            
            case "🐋":
                return left > right
            
            case "🐬":
                return left >= right
            
            case "🐢":
                return left >= right
            
            case "🐊":
                return left >= right
            
            case "🔎":
                return left == right
            
            case "⛔🔎":
                return left != right
             
            case "🔗":
                return left and right
               
            case "⛓️":
                return left or right

class AssignNode(LeafNode):
    def __init__(self, name, value, var_type):
        super().__init__(value)
        self.name = name
        self.var_type = var_type
    
    def evaluate():
        # registers name : value pair in lookup dict
        pass
    
   
            
class UnaryOperatorNode(Node):
    
    def __init__(self, op, exp):
        self.op = op
        self.exp = exp
    
    def evaluate(self):
        value = self.exp.evaluate()
        
        match self.op:
            
            case "⛔":
                
                if isinstance(value, int) or isinstance(value, float):
                    return -1 * value
                
                if isinstance(value, bool):
                    return not value
                
                
class FunctionDef:
    def __init__(self):
        self.name = None
        self.args = []
        self.body = []
        
    def evaluate(self):
        #creates a subtree, and evaluates that
        pass
    
    
class IfNode(FunctionDef):
    def __init__(self, conditional, body):
        super.__init__(None, body)
        self.conditional = conditional

class IfElseNode(IfNode):
    def __init__(self, conditional, body, else_body):
        super().__init__(conditional, body)
        self.else_body = else_body
         
class LoopNode(IfNode):
    def __init__(self, conditional, body):
        IfNode.__init__(conditional, body)
        

                      
class CallNode(LeafNode):
    def __init__(self, name):
        super().__init__(name)
        
    def evaluate(self):
        #lookup value of self, then return 
        pass
  
                
class Literal(LeafNode):
    def __init__(self, literal_type, value):
        super().__init__(value)
        self.literal_type = literal_type
        
    def evaluate(self):
        return self.literal_type(self.value)
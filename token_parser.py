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
                
class KeywordNode(LeafNode):
    def __init__(self, name):
        super().__init__(name)
        
    def evaluate(self):
        #lookup value of self, then return 
        pass
  
                
class IntegerLiteral(LeafNode):
    def __init__(self, value):
        super().__init__(value)
        
    def evaluate(self):
        return int(self.value)
    
    
class StringLiteral(LeafNode):
    def __init__(self, value):
        super().__init__(value)
        
    def evaluate(self):
        return str(self.value)
    

class BooleanLiteral(LeafNode):
    def __init__(self, value):
        super().__init__(value)
        
    def evaluate(self):
        return bool(self.value)
    
    
class FloatLiteral(LeafNode):
    def __init__(self, value):
        super().__init__(value)
        
    def evaluate(self):
        return float(self.value)
                 

            


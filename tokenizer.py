import regex

tokens = [
    ("WHITESPACE", r"\s+"),
    ("COMMENT", r"💭.*?💭"),
    ("BOOLEAN", r"True|False"),
    ("FLOAT", r'\d+\.\d+'),
    ("INTEGER", r"\d+"),
    ("OPERATOR", r"\+|-|/|\*|==|!=|>|<|>=|<=|\+=|-=|\*="),
    ("STRUCTURE", r"🙂|😴|➡️|⬅️|⏩|⏪|⏭️|⏮️|🔄️|🚫"),
    ("STRING", r'\\\".*\\"'),
    ("KEYWORD", r"\w+|\p{Emoji}+")
]

IGNORE = ["WHITESPACE", "COMMENT"]



class Token:
    
    def __init__(self, type, value):
        self.type = type
        self.value = value
        
class Tokenizer:
    def __init__(self):
        self.tokenized = []
       
    def tokenize(self, code):
        position = 0
        
        while position < len(code):
            matched = None
            
            for token_type, pattern in tokens:
                reg = regex.compile(pattern)
                matched = reg.match(code, position)
                
                if matched:
                    token_value = matched.group(0)
                    
                    if token_type not in IGNORE and token_value != "\uFE0F":
                        self.tokenized.append(Token(token_type, token_value))
                    
                    position = matched.end()
                    break
                
            if not matched:
                raise ValueError(f"Unrecognized symbol at {position}")            


if __name__ == "__main__":
    test = Tokenizer()
    test.tokenize("")
    for token in test.tokenized:
        print(f"Type: {token.type}, Value: {token.value}")


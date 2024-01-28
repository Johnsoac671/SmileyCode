import regex

tokens = [
    ("WHITESPACE", r"\s+"),
    ("BOOLEAN", r"True|False"),
    ("FLOAT", r'\d+\.\d+'),
    ("INTEGER", r"\d+"),
    ("STRUCTURE", r"🙂|😴|➡️|⬅️|⏩|⏪|⏭️|⏮️|🔄️|🚫"),
    ("STRING", r'\\\".*\\"'),
    ("IDENTIFIER", r"\w+|\p{Emoji}+")
    
]





class Token:
    
    def __init__(self, type, value):
        self.type = type
        self.value = value
        
def tokenize(code):
    position = 0
    tokenized = []
    
    while position < len(code):
        matched = None
        
        for token_type, pattern in tokens:
            reg = regex.compile(pattern)
            matched = reg.match(code, position)
            
            if matched:
                token_value = matched.group(0)
                
                if token_type != "WHITESPACE" and token_value != "\uFE0F":
                    tokenized.append(Token(token_type, token_value))
                
                position = matched.end()
                break
            
        if not matched:
            raise ValueError(f"Unrecognized symbol at {position}")
        
    return tokenized

result = tokenize(r"🙂 ⚙️ 👁️ ⏩ \"Hello, World!\" ⏪ 🚫 😴")

for token in result:
    print(f"Type: {token.type}, Value: {token.value}")


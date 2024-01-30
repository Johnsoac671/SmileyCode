import regex

tokens = [
    ("WHITESPACE", r"\s+"),
    ("COMMENT", r"💭.*?💭"),
    ("BOOLEAN", r"✅|❌"),
    ("FLOAT", r'\d+\.\d+'),
    ("INTEGER", r"\d+"),
    ("OPERATOR", r"\+|-|/|\*|🔎|⛔|🐋|🐢|🐬|🐊"),
    ("STRUCTURE", r"🙂|😴|➡️|⬅️|⏩|⏪|⏭️|⏮️|🔄️|🚫|\(|\)|💡"),
    ("TYPE", r"⚙️|🧵|🧮|🎳|👻"),
    ("STRING", r'\\"(.*?)\\"'),
    ("KEYWORD", r"\w+|\p{Emoji}+")
]

IGNORE = ["WHITESPACE", "COMMENT"]



class Token:
    
    def __init__(self, type, value):
        self.type = type
        self.value = value
        
class Tokenizer:
    def __init__(self, code):
        self.tokenized = self.tokenize(code)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            return self.tokenized.pop()
        except IndexError:
            raise StopIteration
    
    def peek(self):
        return self.tokenized[-1]
       
    def tokenize(self, code):
        code.replace("\"", "\\\"")
        position = 0
        
        tokenized = []
        
        while position < len(code):
            matched = None
            
            for token_type, pattern in tokens:
                reg = regex.compile(pattern)
                matched = reg.match(code, position)
                
                if matched:
                    token_value = matched.group(0)
                    
                    if token_type not in IGNORE and token_value != "\uFE0F":
                        tokenized.append(Token(token_type, token_value))
                    
                    position = matched.end()
                    break
                
            if not matched:
                raise ValueError(f"Unrecognized symbol at {position}: {code[position]}")            

        return tokenized[::-1]


if __name__ == "__main__":
    test = Tokenizer(r"🙂 📝 ⚙️ getWordCount ⏩ arg1 ⏪ 🟰 ⏭️ 📝 🧮 index 🟰 0 🚫 📝 🧮 count 🟰 0 🚫 🔄️ (index 🐢 (⚙️ 📏 ⏩ arg1 ⏪)) ⏭❔ (arg1 📌 index 🔎 \" \" ) 👉 ⏭️ count 🟰 count ➕ 1 🚫 ⏮️ index 🟰 index ➕ 1 ⏮️ 🔄️ 🚫 ↩️ count ⏮️ 🚫 📝 🧮 count 🟰 ⚙️ getWordCount ⏩ \"This is my sentence\" ⏪ 🚫 ⚙️ 👁️ ⏭️ count ⏮️ 🚫 😴")
    for token in test:
        print(f"Type: {token.type}, Value: {token.value}")


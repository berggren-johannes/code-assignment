class FileParser:
    def __init__(self, text):
        self.text = text
        self.prefix = "foo"
        self.suffix = "bar"

    def get_raw(self):
        return self.text
    
    def get_parsed(self):
        return self.text.split()
    
    def get_most_common_word(self):
        words = self.get_raw()
        return words
    
    def sandwich_word(self, word):
        return f"{self.prefix}{word}{self.suffix}"
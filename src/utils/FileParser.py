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
        
        # Split the text into words
        words = words.split()

        if len(words) == 0:
            raise ValueError("No words found")

        # Count the frequency of each word
        words.sort()

        # Find the word with the highest frequency
        most_common_word = words[0]
        # Return the word with the highest frequency

        return most_common_word
    
    def sandwich_word(self, word):
        return f"{self.prefix}{word}{self.suffix}"
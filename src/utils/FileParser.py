import re

class FileParser:
    def __init__(self, text):
        self.text = text
        self.prefix = "foo"
        self.suffix = "bar"
    
    def get_parsed(self):
        replaced_text = self.replace_words()
        return replaced_text
    
    def get_most_common_word(self):
        words = self.text
        words = words.split()

        if len(words) == 0:
            raise ValueError("Text file is empty")

        special_char_pattern = r"[^a-zA-Z0-9]"
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            elif re.search(special_char_pattern, word) is None:
                word_count[word] = 1

        word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))

        if len(word_count) > 1:
            multiple_words = [list(word_count.keys())[0]]
            word_keys = list(word_count.keys())

            for i in range(1, len(word_keys)):
                if word_count[word_keys[i]] == word_count[word_keys[i - 1]]:
                    multiple_words.append(word_keys[i])
                else:
                    break
            return multiple_words
                
        most_common_word = [list(word_count.keys())[0]]

        return most_common_word
    
    def replace_words(self):
        if len(self.text) == 0:
            raise ValueError("No text to replace words in")
        
        words = self.get_most_common_word()
        if len(words) == 0:
            raise ValueError("Words list is empty")
            
        parsed_text = self.text
        for word in words:
            parsed_text = re.sub(rf"\b{word}\b", self.prefix + word + self.suffix, parsed_text, flags=re.IGNORECASE)

        return parsed_text
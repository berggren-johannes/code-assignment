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
        words = words.split()

        if len(words) == 0:
            raise ValueError("Text file is empty")

        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))

        print(word_count)

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
    
    def sandwich_word(self, text, words):
        if len(text) == 0:
            raise ValueError("No text to replace words in")
        
        if len(words) == 0:
            raise ValueError("Words list is empty")

        parsed_text = text
        for word in words:
            parsed_text = parsed_text.replace(word, f"{self.prefix}{word}{self.suffix}")

        return parsed_text